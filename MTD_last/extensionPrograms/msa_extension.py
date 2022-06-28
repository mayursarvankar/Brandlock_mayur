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



def msa_extension(urlList):
    driver_obj=driverExtenstio("msa")

    Resurllist = []

    for url in urlList:

        driver_obj.get(url)

        set_cookie(drivar_obj=driver_obj, cookie_name="_blka_uab", cookie_value="101")

        driver_obj.refresh()

        page_is_loading(driver_obj)

        time.sleep(5)

        # driver_obj.execute_script("alert('page is loaded')")

        try:
            iframe_msa = driver_obj.find_element(By.CSS_SELECTOR, "#psa-in-page")
            switch_frame = driver_obj.switch_to.frame(iframe_msa)

            while True:
                time.sleep(1)
                clik_chck = driver_obj.find_element(By.CSS_SELECTOR, ".message.ellipsis")
                if clik_chck is not None:
                    break

            clik = driver_obj.find_element(By.CSS_SELECTOR, ".message.ellipsis")
            if clik.text == 'More like this':
                clik.click()

                time.sleep(2)

                # print(f'clik --> {clik}')
                msa_count = 'msa_present'
                Resurllist.append(msa_count)
            else:
                msa_count = 'msa_absent'
                Resurllist.append(msa_count)


        except:
            msa_count = 'msa_absent'
            Resurllist.append(msa_count)


        if msa_count =='msa_present':break



    result = Resurllist[-1]

    return result, driver_obj







# web_url="https://cariuma.com/collections/the-catiba-pro-mens/products/catiba-pro-off-white-black-canvas-sneaker-men"
# web_url=['https://www.cartier.com/en-us/jewelry/necklaces/symbol-pendant-CRB3153111.html',
#             'https://us.currentbody.com/products/t3-cura-luxe-ionair-hairdryer',
#             'https://www.jiffyshirts.com/portauthority-GL01.html?ac=Black',
#          'https://cariuma.com/collections/the-catiba-pro-mens/products/catiba-pro-off-white-black-canvas-sneaker-men']
#
#
# print(msa_extension(web_url))