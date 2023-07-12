import requests
import re
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from core.celery import app
from core.product.models import Product


BASE_URL = "https://world.openfoodfacts.org"

def collect_errors(error):
    return {"success": False, "error": error}

@app.task(bind=True, ignore_result=True, retry=True, retry_policy={
        'max_retries': 5,
        'interval_start': 0,
        'interval_step': 0.2,
        'interval_max': 0.5,
    })
def create_product(self, product):
    try:
        product = Product.objects.get_or_create(code=product["code"], defaults=product)
        if product:
            return {"success": True}
    except Exception as e:
        return collect_errors(e)


def scrape_product_details(product_link):
    try:
        response = requests.get(product_link)
        soup = BeautifulSoup(response.content, "html.parser")
        product_details = {}
        product_details["code"] = int(soup.find( id="barcode").text.strip())
        product_details["product_name"] = (soup.find("h2", class_="title-1").text).strip()
        product_details["status"] = Product.Status.IMPORTED
        product_details["barcode"] = (soup.find( id="barcode_paragraph").text).split(":")[-1].strip()
        product_details["quantity"] = soup.find( id="field_quantity_value").text
        product_details["categories"] = soup.find( id="field_categories_value").text
        product_details["packaging"] = soup.find( id="field_packaging_value").text
        product_details["brands"] = soup.find( id="field_brands_value").text
        product_details["image_url"] = soup.find("img", class_="product_image").get("src")
        return product_details
    except requests.exceptions.RequestException as e:
        return collect_errors(e)
    except Exception as e:
        return collect_errors(e)

@app.task(bind=True, ignore_result=True, retry=True, retry_policy={
        'max_retries': 5,
        'interval_start': 0,
        'interval_step': 0.2,
        'interval_max': 0.5,
    })
def scrape_products(self, max_products=100):
    products = []
    page_num = 1
    while len(products) < max_products:
        url = f"{BASE_URL}/{page_num}"
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            product_urls = soup.select('.products li a')
            for product_url in product_urls:
                product = scrape_product_details(product_url["href"])
                products.append(product)
                time = (datetime.now + timedelta(seconds=5))
                create_product.apply_async(args=[product], eta=time)
            page_num += 1
        except requests.exceptions.RequestException as e:
            break
        except Exception as e:
            break


# def scrape_products(page_number):
#     products = []
#     url = f"{BASE_URL}/{page_number}"
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         soup = BeautifulSoup(response.content, "html.parser")
#         product_links = soup.select('.products li')
        
#         for link in product_links:
#             product_draft = {
#                 "url": link.find("a").get("href"),
#                 "product_name": link.find("span").text,
#                 "status": Product.Status.DRAFT
#             }
#             code = extract_code_from_url(product_draft["url"])
            
#             if code:
#                 product, created = Product.objects.get_or_create(code=code, defaults=product_draft)
#                 if created:
#                     products.append(product)
                    
#         return products
#     except requests.exceptions.RequestException as e:
#         print(f"Error occurred while scraping products: {str(e)}")
#         return []


# def scrape_product_details(product_link):
#     response = requests.get(product_link)
#     soup = BeautifulSoup(response.content, "html.parser")
#     product_details = {}
#     product_details["barcode"] = (soup.find( id="barcode_paragraph").text).split(":")[-1].strip()
#     product_details["quantity"] = soup.find( id="field_quantity_value").text
#     product_details["categories"] = soup.find( id="field_categories_value").text
#     product_details["packaging"] = soup.find( id="field_packaging_value").text
#     product_details["brands"] = soup.find( id="field_brands_value").text
#     product_details["image_url"] = soup.find("img", class_="product_image").get("src")
#     return product_details

# def get_products():
#     products_links = scrape_products(1)
#     for product_link in products_links:
#         print(product_link)
        