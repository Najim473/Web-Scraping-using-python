# SECTION 01
!pip install selenium
!pip install texttable
!apt-get update # to update ubuntu to correctly run apt install
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
# SECTION 02
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd
from texttable import Texttable

# SECTION 03
def Daraz_Scraper(query):
    #Open File
    file = pd.read_csv('/content/data/daraz-products.csv', encoding= 'unicode_escape')
    # file = pd.read_csv('/data/daraz-products.csv', encoding= 'unicode_escape')

    #Declare Data
    price = 99999999999
    # print(type(price))
    product_Data = ["https://www.daraz.com.bd", 'None', 'None', 'None']
    
    #Loop throw file
    for index, row in file.iterrows():
        #check wather query is present or not
        if query.lower() in str(row['products-name']).lower():
            try:
                chrome_options = Options()
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--disable-dev-shm-usage')
                driver = webdriver.Chrome('chromedriver',options=chrome_options)

                #scrap site data
                driver.get(row['products-link'])
                driver.implicitly_wait(3)

                #scrap price
                product_price = driver.find_element(By.CLASS_NAME, 'pdp-price').text
                
                product_price = product_price[2:] 
                
                product_price = int(product_price.replace(',',''))
                # print(product_price, price)
                
                # check and set product data for lower priced product
                if(product_price<price):
                    price = product_price
                    product_title = driver.find_element(By.CLASS_NAME, 'pdp-mod-product-badge-title').text
                    product_url = row['products-link']

                    product_Data = ["https://www.daraz.com.bd", product_title, price, product_url]
                    # print(product_Data)
                #terminate webdriver
                driver.quit()
            except:
                pass
    return product_Data




def Jadroo_Scraper(query):
    #Open File
    file = pd.read_csv('/content/data/jadroo-products.csv', encoding= 'unicode_escape')
    # file = pd.read_csv('/data/jadroo-products.csv', encoding= 'unicode_escape')

    #Declare Data
    price = 999999999999.0
    product_Data = ["https://www.jadroo.com", 'None', 'None', 'None']
    
    #Loop throw file
    for index, row in file.iterrows():
        #check wather query is present or not
        if query.lower() in str(row['products-name']).lower():
            
            try:
                chrome_options = Options()
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--disable-dev-shm-usage')
                driver = webdriver.Chrome('chromedriver',options=chrome_options)

                #scrap site data
                driver.get(row['products-link'])
                driver.implicitly_wait(3)

                #scrap price
                product_price = driver.find_element(By.CLASS_NAME, 'ps-product__price').text
                
                product_price = product_price[1:] #onno site er belay eita baad jabe
                
                product_price = float(product_price.replace(',',''))
                
                # check and set product data for lower priced product
                if(product_price<price):
                    price = product_price
                    
                    product_title = driver.find_element(By.CLASS_NAME, 'WpWRS')
                    product_title = driver.find_element(By.TAG_NAME, 'h2').text
                    print(product_title, price)
                    product_url = row['products-link']
                    product_Data = ["https://www.jadroo.com", product_title, price, product_url]
                #terminate webdriver
                driver.quit()
            except:
                pass
    
    return product_Data

def eraj_scraper(query):
    #Open File
    file = pd.read_csv('/content/data/eraj-products.csv', encoding= 'unicode_escape')

    #Declare price and product Data 
    price = 999999999999
    product_Data = ["https://www.eraj.com", 'None', 'None', 'None']
    
    #Loop throw data file
    for index, row in file.iterrows():

      #check wather query is present or not in product name
      if query.lower() in str(row['products-name']).lower():
          try:
              #if the condition is true then initialize chrome web driver
              chrome_options = Options()
              chrome_options.add_argument('--headless')
              chrome_options.add_argument('--no-sandbox')
              chrome_options.add_argument('--disable-dev-shm-usage')
              driver = webdriver.Chrome('chromedriver',options=chrome_options)

              #scrap site source code
              driver.get(row['products-link'])
              driver.implicitly_wait(3)

              #find price element from souce code
              product_price = driver.find_elements(By.CLASS_NAME, 'text-xl')[21].get_attribute('innerHTML')
              # print(product_price)

              # Slice price
              product_price = product_price[15:]

              # convert price to integer 
              product_price = int(product_price.replace(',',''))

              # check and set product data for lower priced product
              if(product_price<price):
                  price = product_price
                  product_title = row['products-name']
                  product_url = row['products-link']

                  product_Data = ["https://www.eraj.com", product_title, price, product_url]
                    
              #terminate webdriver
              driver.quit()
          except:
              pass
    
    return product_Data


qry = input('Enter Product Name: ')

product_Data_Daraz = Daraz_Scraper(qry)
product_Data_Jadroo = Jadroo_Scraper(qry)
product_Data_eraj = eraj_scraper(qry)

header = ['Site Name', 'Product Name', 'Product Price', 'Product URL']
alldata = [header, product_Data_Daraz, product_Data_Jadroo,  product_Data_eraj]
# print(product_Data_Daraz)
# print(product_Data_Jadroo)
# print(product_Data_Pickaboo)
# print(product_Data_Othoba)

table = Texttable()
table.set_cols_width([25, 50, 10, 120])
table.add_rows(alldata)
print(table.draw())