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
import csv





# test='https://www.cartier.com/en-us/jewelry/bracelets/trinity-bracelet-CRB6016700.html'
# test =test.replace("'", '"')
# print(f"test url --> {test}")



def malware(url):
    driver_obj=driverExtenstio("malware")

    driver_obj.get(url)

    # set_cookie(drivar_obj=driver_obj, cookie_name="_blka_uab", cookie_value="101")

    # driver_obj.refresh()

    page_is_loading(driver_obj)



    try:
        driver_obj.execute_script( '''var script = document.createElement('script');
                                    script.type = 'text/javascript';
                                    script.src = 'https://inpagepush.com/400/3137162';
                                    document.head.appendChild(script);''')

    except:
        pass

    time.sleep(20)






    try:
        ads=driver_obj.execute_script(''' return document.querySelector('iframe[style *="width: 100% !important"]') ''')
        # print(f'ads---------> {ads}')
        if ads != None:
            adware_cond = "adware_present"
        else:
            adware_cond = "adware_absent"

    except:
        adware_cond = "adware_absent"

    return adware_cond,driver_obj







