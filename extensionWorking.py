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


# "https://crxextractor.com/"
# options = webdriver.ChromeOptions()
# # options.add_extension("D:\\extension_3_0_8_0.crx") # <---
# # OP=options
# driver=webdriver.Chrome(executable_path = "chromedriver.exe",options=options)
# driver.get("https://google.com")
#
# n = 2
# actions = ActionChains(driver)
# actions.send_keys(Keys.TAB * n)
# actions.perform()

# driver=webdriver.Chrome(executable_path = "chromedriver.exe")



options = webdriver.FirefoxOptions()
# options.add_extension("D:\\extension_3_0_8_0.crx") # <---
# OP=options
driver=webdriver.Firefox(executable_path = "geckodriver.exe",options=options)
driver.get("https://google.com")
actions = ActionChains(driver)
actions.send_keys(Keys.F12)
actions.perform()
