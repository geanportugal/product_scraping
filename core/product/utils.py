import requests
import re
from bs4 import BeautifulSoup, element
from django.conf import settings
from django.core.mail import send_mail
from core.product.models import Product


def send_mail_error(url, error):
    send_mail(
        "Error when integrating product",
        f"Url: {url} - Error: {error}",
        settings.EMAIL_ADMIN,
        settings.EMAIL_ADMIN,
        fail_silently=True,
    )
    


def extract_code_from_url(url):
    """Extracts the code from the given URL."""
    match = re.search(r'/product/(\d+)/', url)
    return match.group(1) if match else None

def collect_errors(error):
    return {"success": False, "error": error}

def result_to_text(value):
    if isinstance(value, element.Tag):
        return value.text
    return None


def scrape_products_list():
    products = []
    page_num = 1
    while len(products) < settings.MAX_PRODUCTS:
        url = f"{settings.BASE_URL}/{page_num}"
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            products_list= soup.select('.products li')
            for product in products_list:
                product_url = (lambda product: product.find("a").get("href") \
                    if product.find("a").get("href") else None)(product)
                if not product_url:
                    continue
                product_draft = {
                    "url": f"{settings.BASE_URL}{product_url}",
                    "code": extract_code_from_url(product_url),
                    "product_name": product.find("span").text,
                }
                products.append(product_draft)
        except requests.exceptions.RequestException as e:
            send_mail_error(url, e)
            break
        except Exception as e:
            send_mail_error(url, e)
            break
    return products
            

def scrape_product_details(product_link):
    try:
        response = requests.get(product_link)
        soup = BeautifulSoup(response.content, "html.parser")
        product_details = {}
        product_details["barcode"] = result_to_text(soup.find( id="barcode_paragraph")).strip()
        product_details["quantity"] = result_to_text(soup.find( id="field_quantity_value"))
        product_details["categories"] = result_to_text(soup.find( id="field_categories_value"))
        product_details["packaging"] = result_to_text(soup.find( id="field_packaging_value"))
        product_details["brands"] = result_to_text(soup.find( id="field_brands_value"))
        product_details["image_url"] = (
            lambda soup: soup.find("img", class_="product_image").get("src") \
                if soup.find("img", class_="product_image") else None
            )(soup)

        return product_details
    except requests.exceptions.RequestException as e:
        send_mail_error(product_link, e)
        return {}
    except Exception as e:
        send_mail_error(product_link, e)
        return {}
    

def create_or_update_product(product):
    product.update({'status':  Product.Status.IMPORTED })
    if any(value is None for value in product.values()):
        product['status'] = Product.Status.DRAFT      
    obj, created = Product.objects.update_or_create(
    code=product['code'],
    defaults=product,
)
