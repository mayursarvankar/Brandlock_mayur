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
from  MTD_last.util import *
import os





# test='https://www.cartier.com/en-us/jewelry/bracelets/trinity-bracelet-CRB6016700.html'
# test =test.replace("'", '"')
# print(f"test url --> {test}")



def stirfy_extension(urlList):
    driver_obj =driverExtenstio("stirfy")

    Resurllist = []

    for url in urlList:
        driver_obj.get(url)

        set_cookie(drivar_obj=driver_obj, cookie_name="_blka_uab", cookie_value="101")

        driver_obj.refresh()

        page_is_loading(driver_obj)

        # driver_obj.execute_script("alert('page is loaded')")

        time.sleep(10)

        try:
            driver_obj.execute_script(
                '''document.querySelector('#openPriceDeals').click()''')

            time.sleep(5)
            stirfy_count = 'stirfy_present'
            Resurllist.append(stirfy_count)

        except:
            stirfy_count = 'stirfy_absent'
            Resurllist.append(stirfy_count)

        if stirfy_count == 'stirfy_present' :break


    result = Resurllist[-1]

    return result, driver_obj






# web_url="https://cariuma.com/collections/the-catiba-pro-mens/products/catiba-pro-off-white-black-canvas-sneaker-men"
# web_url=['https://www.footwearetc.com/products/pedifix-visco-gel-hammer-toe-cushion-unisex']
# print(stirfy_extension(web_url))