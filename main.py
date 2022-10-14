from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# DARAZ
# from all_scraper import scrap_daraz
# categorie_name = "Smart phone"
# categorie_link = "https://www.daraz.com.bd/smartphones/?page=1&spm=a2a0e.home.cate_6.1.735212f7OSOpJr"
# page_upto = 2
# scrap_daraz(categorie_name, categorie_link, page_upto)

# JADROO
# from all_scraper import scrap_jadroo
# categorie_name = "smart-phones"
# category_slug= "smart-phones"
# page_upto = 5
# scrap_jadroo(categorie_name, category_slug, page_upto)

# Eraj 
from all_scraper import scrap_eraj
categorie_name = "Freezer"
page_upto = 5
categorie_id = 7 
scrap_eraj(categorie_id, categorie_name, page_upto)