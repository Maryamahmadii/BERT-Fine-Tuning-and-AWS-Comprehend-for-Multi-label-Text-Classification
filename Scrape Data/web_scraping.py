from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import csv
import pandas as pd


url = "https://URL/"  # Replace with the actual URL if needed
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

categories_container = soup.find('ul', class_='head-dd js-head-depts')

categories = []

# Extract each category's name and URL
for category_li in categories_container.find_all('li', class_='item js-head-dept'):
    a_tag = category_li.find('a', class_='head-dd-main')
    if a_tag:
        category_name = a_tag.text.strip()
        category_url = url + a_tag['href']  # Assuming relative URLs which need the base URL
        categories.append({'name': category_name, 'url': category_url})

# Test: Now you have a list of category names and their URLs
for category in categories:
    print(f"Category Name: {category['name']}, URL: {category['url']}")

# Function to get subcategories
def get_subcategories(category_url):
    response = requests.get(category_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    ul_element = soup.find('ul', class_='ptype-grid -col-6 -tile')
    subcategories = []

    if ul_element:
        li_elements = ul_element.find_all('li', class_='li')

        for li in li_elements:
            a_tag = li.find('a', class_='ptype-grid-a -descr-outer')  # Find the 'a' tag with the specific class
            if a_tag and 'href' in a_tag.attrs:
                # Extract the text and URL from the 'a' tag
                name = a_tag.text.strip()
                url = urljoin(category_url, a_tag['href'])
                subcategories.append({'name': name, 'url': url})

    return subcategories

# Function to get sub-subcategories
def get_sub_subcategories(subcategory_url):
    response = requests.get(subcategory_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the main container for sub-subcategories, similar to how we found subcategories
    sub_subcategories_container = soup.find('ul', class_='ptype-grid -col-6 -tile')
    sub_subcategories = []

    # If the container exists, find all 'li' elements representing the sub-subcategories
    if sub_subcategories_container:
        li_elements = sub_subcategories_container.find_all('li', class_='li')

        for li in li_elements:
            a_tag = li.find('a', class_='ptype-grid-a -descr-outer')  # Adjust the class name if needed
            if a_tag and 'href' in a_tag.attrs:
                name = a_tag.get('data-descr', '').strip()
                url = urljoin(subcategory_url, a_tag['href'])
                sub_subcategories.append({'name': name, 'url': url})

    return sub_subcategories

# Function to get products
def get_products(sub_subcategory_url):
    response = requests.get(sub_subcategory_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all 'li' elements with class 'js-product-list-item'
    product_items = soup.find_all('li', class_='js-product-list-item')

    products = []
    for item in product_items:
        # Extracting product name
        name_tag = item.find('span', class_='lst-a-name')
        product_name = name_tag.get_text(strip=True) if name_tag else 'No Name'

        # Extracting product URL
        url_tag = item.find('a', class_='lst-a')
        product_url = urljoin(sub_subcategory_url, url_tag['href']) if url_tag and 'href' in url_tag.attrs else 'No URL'

        # Extracting product price
        price_tag = item.find('span', class_='lst-prc')
        product_price = price_tag.get_text(strip=True) if price_tag else 'No Price'

        products.append({'name': product_name, 'url': product_url, 'price': product_price})

    return products

def fetch_categories(base_url):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    categories_container = soup.find('ul', class_='head-dd js-head-depts')
    categories = []
    for category_li in categories_container.find_all('li', class_='item js-head-dept'):
        a_tag = category_li.find('a', class_='head-dd-main')
        if a_tag:
            category_name = a_tag.text.strip()
            category_url = urljoin(base_url, a_tag['href'])
            categories.append({'name': category_name, 'url': category_url})
    return categories


def fetch_all_data(base_url):
    categories = fetch_categories(base_url)
    for category in categories:
        subcategories = get_subcategories(category['url'])
        category['subcategories'] = subcategories
        for subcat in category['subcategories']:
            sub_subcategories = get_sub_subcategories(subcat['url'])
            subcat['sub_subcategories'] = sub_subcategories
            for sub_subcat in subcat['sub_subcategories']:
                products = get_products(sub_subcat['url'])
                sub_subcat['products'] = products
    return categories

def write_data_to_csv(data):
    headers = ['Main Category', 'Subcategory', 'Sub-Subcategory', 'Product Name', 'URL', 'Price']
    with open('products.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for category in data:
            for subcat in category.get('subcategories', []):
                for sub_subcat in subcat.get('sub_subcategories', []):
                    for product in sub_subcat.get('products', []):
                        writer.writerow({
                            'Main Category': category['name'],
                            'Subcategory': subcat['name'],
                            'Sub-Subcategory': sub_subcat['name'],
                            'Product Name': product['name'],
                            'URL': product['url'],
                            'Price': product['price']
                        })

base_url = "https://URL.com/"
all_data = fetch_all_data(base_url)
write_data_to_csv(all_data)