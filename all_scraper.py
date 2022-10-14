from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import csv
import requests
# from pathlib import Path
# print(Path.cwd())

def scrap_daraz(categorie_name, categorie_link, page_upto):
    #initialize driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    #implicit wait
    driver.implicitly_wait(0.5)
    #maximize browser
    driver.maximize_window()
    #declare file name and open file
    filename = '/Users/najim/PycharmProject/pythonProject/data/daraz-products.csv'
    url = categorie_link
    position_to_replace = categorie_link.find("page=")
    with open(filename, 'a', newline='', encoding = 'utf-8') as f:
        # create file header
        w = csv.DictWriter(f,['category','products-name','products-link'])
        w.writeheader()
        i=1
        while(i<=page_upto):
            driver.implicitly_wait(1)
            driver.get(url)
            driver.implicitly_wait(1)
            items = driver.find_elements(By.CLASS_NAME, 'title--wFj93')
            for item in items:
                field = item.find_element(By.TAG_NAME, 'a')
                products_url = field.get_attribute('href')
                products_name = field.get_attribute('innerHTML')
                data = {}
                data['category'] = categorie_name
                data['products-name'] = products_name
                data['products-link'] = products_url
                print(data)
                w.writerow(data)
            i+=1
            # Generate next page url
            url = url[:position_to_replace+5]+str(i)+url[position_to_replace+6:]
        f.close()


def scrap_jadroo(categorie_name, category_slug, page_upto):
    # declare file name and open file
    filename = './data/jadroo-products.csv'
    with open(filename, 'a', encoding = 'utf-8', errors = 'ignore', newline='') as f:
        # create file header
        w = csv.DictWriter(f,['category','products-name','products-link'])
        w.writeheader()

        i=1
        while(i<=page_upto):
            # generate url
            url = "https://contents.jadroo.com/api/v1/category/products?category_slug={}&sorting=&page={}".format(category_slug,i)
            res = requests.get(url).json()
            for item in res["results"]["products"]["data"]:
                data = {}
                data['category'] = categorie_name
                data['products-name'] = item["name"]
                data['products-link'] = "https://www.jadroo.com/products/"+ item["product_slug"]
                print(data['products-name'])
                w.writerow(data)
            i+=1
        f.close()


def scrap_eraj(categorie_id,categorie_name,page_upto):
    # declare file name and open file
    filename = './data/eraj-products.csv'
    with open(filename, 'a', encoding = 'utf-8', errors = 'ignore', newline='') as f:
        w = csv.DictWriter(f,['category','products-name','products-link'])
        w.writeheader()
        i=1
        while(i<=page_upto):
            url = "https://www.eraj.com/category-products/{}?page={}".format(categorie_id, i)
            print("Page No: ", i, url)
            res = requests.get(url).json()
            for item in res["products"]:
                data = {}
                data['category'] = categorie_name
                data['products-name'] = item["name"]
                data['products-link'] = "https://eraj.com/"+ item["slug"]
                print(data['products-name'])
                w.writerow(data)
            i+=1
        f.close()