import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time, datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui
import tldextract
import  glob
from pyshadow.main import Shadow
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import numpy as np
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pandas as pd
from selenium.webdriver.common.keys import Keys
from bs4 import  BeautifulSoup
import csv

with open("amaazon_op.csv", "a", newline="", encoding="UTF-8") as fp:
    writer = csv.writer(fp)
    writer.writerow(["Product_name", "Product_price","Product_website"])

driver_path=os.getcwd().replace("ecomerce","chromedriver.exe")

driver=webdriver.Chrome(executable_path =driver_path)
driver.get("https://www.amazon.in/s?k=organic+jaggery+cubes&i=grocery&crid=68KU0Y0A9N56&sprefix=organic+jaggery+cubes%2Cgrocery%2C379&ref=nb_sb_noss_1")

soupp=BeautifulSoup(driver.page_source)
driver.quit()
# print(soupp)
cards=soupp.select('div[class *="a-section a-spacing-small s-padding-left-small s-padding-right-small"]')
# print(cards)

prod_no=0
for prod_item in cards:
    prod_no =prod_no+1
    print(f"==================================={prod_no}=====================================")
    # print(prod_item)
    prod_name_selecotor='a[class *="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]'
    price_selector=".a-price-whole"

    try:
        prod_name=prod_item.select_one(prod_name_selecotor).text
    except:
        prod_name=""

    try:
        prod_url="https://www.amazon.in"+prod_item.select_one(prod_name_selecotor,href=True)['href']
    except:
        prod_url=""





    try:

        prod_price=prod_item.select_one(price_selector).text
    except:
        prod_price=""



    print(prod_name)
    print(prod_price)
    print(prod_url)

    with open("amaazon_op.csv", "a", newline="", encoding="UTF-8") as fp:
        writer = csv.writer(fp)
        writer.writerow([prod_name, prod_price,prod_url])

    # print(prod_price)
# cards=driver.find_elements(By.CSS_SELECTOR,'div[data-asin*="B"]')

# time.sleep(30)
#
# for prod_item in cards:
#     prod_name=prod_item.find_element(By.CSS_SELECTOR,"a[class *= 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']").text
#     print(prod_name)


"chenanged"