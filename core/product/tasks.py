import requests
import re
import json
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from core.celery import app
from core.product.models import Product
from .utils import (collect_errors, scrape_product_details, 
                    create_or_update_product, scrape_products_list)


@app.task(bind=True, ignore_result=True, retry=True, retry_policy={
        'max_retries': 5,
        'interval_start': 0,
        'interval_step': 0.2,
        'interval_max': 0.5,
    })
def create_or_update_product_task(self, product):
    create_or_update_product(product)


@app.task(bind=True, ignore_result=True, retry=True, retry_policy={
        'max_retries': 5,
        'interval_start': 0,
        'interval_step': 0.2,
        'interval_max': 0.5,
    })
def scrape_products_task(self):
    products = scrape_products_list()
    for product in products:
        product.update(scrape_product_details(product['url']))
        create_or_update_product_task.apply_async(args=[product,])
