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
import os
from  MTD_last.util import *



# test='https://www.cartier.com/en-us/jewelry/bracelets/trinity-bracelet-CRB6016700.html'
# test =test.replace("'", '"')
# print(f"test url --> {test}")



def ali_hunter_extension(urlList):
    driver_obj=driverExtenstio("alihunter")

    Resurllist = []

    for url in urlList:
        driver_obj.get(url)

        set_cookie(drivar_obj=driver_obj, cookie_name="_blka_uab", cookie_value="101")

        driver_obj.refresh()

        page_is_loading(driver_obj)

        # driver_obj.execute_script("alert('page is loaded')")

        time.sleep(2)

        try:
            driver_obj.execute_script(
                '''document.querySelector("div[style= 'position: relative; display: flex; align-items: center; padding: 0px; height: var(--ah-height-nav); overflow: hidden; width: 100%;'] >div >div:nth-child(5)").click()''')

            time.sleep(5)
            ali_hunter_count = 'ali_hunter_present'

            Resurllist.append(ali_hunter_count)

        except:
            ali_hunter_count = 'ali_hunter_absent'
            Resurllist.append(ali_hunter_count)



        if ali_hunter_count == "ali_hunter_present": break

    result = Resurllist[-1]

    return result,driver_obj






# web_url="https://evereve.com/"
# web_url=['https://footwearetc.com/collections/mens/products/hoka-one-one-bondi-sr-men-black-black-leather-mens']
# print(ali_hunter_extension(web_url))