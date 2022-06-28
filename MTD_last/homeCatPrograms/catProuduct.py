from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time, datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui
import tldextract
import glob
from pyshadow.main import Shadow
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import numpy as np
import pandas as pd
import csv
import html
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import requests
from bs4 import BeautifulSoup
from lxml import etree
from MTD_last.util import *
# from splash_product_finder import  *






def product_finder(home_url,category_url,driver_var):


    prodlinks = []

    try:
        # driver_var.get(homeurl)



        driver_var.get(category_url)


        # time.sleep(10)
    except Exception as e:
        print(f'error of {category_url} --> {e}')
        driver_var.get('https://www.google.com')

    cat_soup = BeautifulSoup(driver_var.page_source, "lxml")

    # dom = etree.HTML(str(cat_soup))

    prod_elems = cat_soup.findAll('a',href=True)
    # print(prod_elems)
    # print("--------------------------------------------------------------------------------------------------------------")
    # print(f'status code for {category_url} --> {cat_req.status_code}')
    #https://www.curateur.com/
    for prod_elem in prod_elems:
        try:
            prod_link = prod_elem["href"]
        except:
            prod_link = ""

        try:
            prod_link.replace("#", "")
        except:
            pass



        if prod_link != None:
            if prod_link.startswith(home_url):
                prod_link = prod_link
            else:
                prod_link = home_url + prod_link

        prod_link = chck_link(weblink=prod_link, home_url=home_url)

        # print(f'all product link --> {prod_link}')

        if prod_link != None and prod_link != category_url:

            if "/products/" in prod_link or "/product/" in prod_link or '/p/' in prod_link \
                    or '/p_' in prod_link:
                # print(f'all product link --> {prod_link}')

                prodlinks.append(prod_link)

    # try:
    #     prod_urls = np.random.choice(prodlinks, size=1)
    #     prod_url = str(prod_urls[0]).replace("//","/").replace("https:/","https://")
    #     prod_method_ = "keywords matching"
    #
    # except:
    #     prod_url = ""



    if prodlinks == []:
        prod_method_ = '$ currency method'
        prod_elems3 =cat_soup.select('a',href=True)
        #https://www.melissaanddoug.com/shop-by/skill/fine-motor-skills/
        # print(prod_elems3)
        for prod_elem3 in prod_elems3:
            if "$" in str(prod_elem3) or "£" in str(prod_elem3) or "INR" in str(prod_elem3) \
                    or "₹" in str(prod_elem3) or "￥" in  str(prod_elem3) :
                # print(prod_elem3)
                try:
                    prod_link = prod_elem3["href"]
                except:
                    prod_link = ""

                try:
                    prod_link.replace("#", "")
                except:
                    pass

                if prod_link != None:
                    if prod_link.startswith(home_url):
                        prod_link = prod_link
                    else:
                        prod_link = home_url + prod_link

                # print(f' prod_link --> {prod_link}')

                prod_link = chck_link(weblink=prod_link, home_url=home_url)

                # print(f'all product link --> {prod_link}')

                if prod_link != None and prod_link != category_url:
                        # print(f'all product link --> {prod_link}')

                        prodlinks.append(prod_link)





    if prodlinks==[]:
        #
        prod_method_ = '[class *= "product"] a'
        prod_elems2 = cat_soup.select('[class *= "product"] a',href=True)
        #https://rticoutdoors.com/shop/coolers/hard-sided
        # print(prod_elems2)
        for prod_elem2 in prod_elems2:

                try:
                    prod_link = prod_elem2["href"]
                except:
                    prod_link = ""

                try:
                    prod_link.replace("#", "")
                except:
                    pass

                if prod_link != None:
                    if prod_link.startswith(home_url):
                        prod_link = prod_link
                    else:
                        prod_link = home_url + prod_link

                prod_link = chck_link(weblink=prod_link, home_url=home_url)

                if prod_link != None and prod_link != category_url and "/c/" not in prod_link:
                    # print(f'all product link --> {prod_link}')
                    prodlinks.append(prod_link)


    if prodlinks==[] :
        prod_method_=""





    return prodlinks




