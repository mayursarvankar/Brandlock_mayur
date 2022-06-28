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

driver_var = webdriver.Chrome(executable_path=r"deoendecie/chromedriver.exe")
driver_var.maximize_window()


df=pd.read_csv(r"C:\Users\Admin\PycharmProjects\db_conection_screenshot\MTD_Monthly\input_data\test_home.csv")

url_no=0
for id,url in zip(df['Web_id'].values,df['Company_Website']):
    url_no = url_no + 1
    try:
        driver_var.get(url)
    except:
        driver_var.get("https://www.google.com/")

    # time.sleep(10)
    saving_path=r"C:\Users\Admin\PycharmProjects\db_conection_screenshot\MTD_Monthly\programs\Screenshot\website_check_home" + "\\" + str(id) +".png"
    driver_var.get_screenshot_as_file(saving_path)
    print(f"({url_no}). {id} ---> {url}")

    # url_no = url_no +1
    # if url_no==1:
    #     break











