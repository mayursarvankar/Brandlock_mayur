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
from PIL import Image
import pytesseract
import cv2
import easyocr
import pyperclip


with open("reply_output.csv","a",newline="",encoding="UTF-8") as fp:
   writer=csv.writer(fp)
   writer.writerow(["Sr No","First Name","Last Name","Domain Name","Email id","Email Status","Date_time"])

df=pd.read_csv("reply_input.csv")
# ['SrNo', 'Full_Name', 'First_Name', 'Last_Name', 'Designation','Domain']
# company_domain="blackrock.com"
# frist_name="Rashmi"
# last_name="Joshi"

options = webdriver.ChromeOptions()  # Path to your chrome profile
options.add_argument('--profile-directory=Profile 14')

options.add_argument("user-data-dir=C:\\Users\\Admin\AppData\\Local\\Google\\Chrome\\User Data")  # Path to your chrome


driver_var = webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\db_conection_screenshot\drivers\chromedriver.exe", options=options)

driver_var.maximize_window()
# driver_var.set_window_position(-10000,0)




url_no = 0
for Sr_No ,frist_name,last_name,company_domain in zip(df['SrNo'].values,df['First_Name'].values,df['Last_Name'].values,df['Domain'].values):
   Sr_No =int(Sr_No)

   # url_no=url_no+1
   # if url_no ==3:
   #   break

   # print( Sr_No ,frist_name,last_name,company_domain)


   driver_var.get("chrome-extension://amcdijdgmckgkkahhcobikllddfbfidi/pluginSrc/index.html")
   time.sleep(2)
   # driver_var.(By.CSS_SELECTOR, "[data-cy = 'plus-button']").click()
   driver_var.execute_script('''document.querySelector("[data-cy = 'plus-button']").click() ''')

   time.sleep(2)
   # driver_var.find_element(By.CSS_SELECTOR, "[data-cy=add-menu-create-contact]").click()
   driver_var.execute_script(''' document.querySelector("[data-cy=add-menu-create-contact]").click()  ''')
   time.sleep(2)


   email_input=driver_var.find_element(By.CSS_SELECTOR,"input[name=email]")
   first_name_input=driver_var.find_element(By.CSS_SELECTOR,"input[name=firstName]")
   last_name_input=driver_var.find_element(By.CSS_SELECTOR,"input[name=lastName]")

   email_input.send_keys(company_domain)
   first_name_input.send_keys(frist_name)
   last_name_input.send_keys(last_name)

   time.sleep(2)
   # driver_var.find_element(By.XPATH,'//div[@class="src__Box-sc-1sbtrzs-0 src__Flex-sc-1sbtrzs-1 sc-jTzLTM bUPfht"]/*[name()="svg"][@width="17"]').click()

   driver_var.execute_script(''' var event = new MouseEvent('click', {
    'view': window,
    'bubbles': true,
    'cancelable': true
  });
document.querySelector("#content-wrap > div.src__Box-sc-1sbtrzs-0.blGwRa > div.src__Box-sc-1sbtrzs-0.sc-fZwumE.kdvBOi > div > div > svg").dispatchEvent(event); ''')


   #chcking email found or not
   timeout = time.time() + 60 * 1  # 1 minutes from now
   while True:

      try:
         email_status=driver_var.execute_script('''return document.querySelector(".sc-brqgnP.hIoYOw").textContent ''')
      except:
         email_status=""

      # print(f'email_status --> {email_status}')



      email_id_cond = driver_var.execute_script(
         ''' return document.querySelector("#content-wrap >div  >div:nth-child(3) span").textContent ''')

      # print(f'email_id_cond --> {email_id_cond}')

      if email_status == "Email not found." or email_id_cond != company_domain or time.time() > timeout:
         break

   try:
      # email_id=driver_var.find_element(By.CSS_SELECTOR,"#content-wrap >div  >div:nth-child(3) span").text
      email_id=driver_var.execute_script(''' return document.querySelector("#content-wrap >div  >div:nth-child(3) span").textContent ''')

   except Exception as e :
      # print(e)
      email_id=""

   if email_id ==company_domain or email_id == "":
      try:
         driver_var.execute_script(
            ''' document.querySelector("#content-wrap").style.backgroundColor = "#e8e195"  ''')
      except:
         pass
   if  email_id !=company_domain :
      try:
         driver_var.execute_script(
            ''' document.querySelector("#content-wrap").style.backgroundColor = "#05fc05"  ''')
      except:
         pass

   if email_id !=company_domain:
      email_status_var="Email Found"
   else:
      email_status_var = "Email not found"
      email_id=""


   time.sleep(1)



   # pyautogui.click(x=758, y=439)
   # time.sleep(3)
   # pyautogui.click(x=758, y=439)
   # pyautogui.hotkey('ctrl', 'a')
   # pyautogui.hotkey('ctrl', 'c')
   driver_var.get_screenshot_as_file(f"replay_screenshot/{Sr_No}.png")
   #
   #
   # email_id = str(pyperclip.paste())




   current_time=datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')

   print(f"======================{Sr_No}==========================")
   print(f"First name      : {frist_name} \n"
         f"Last name       : {last_name} \n"
         f"Comoany Domain  : {company_domain} \n"
         f"Email Id        : {email_id} \n"
         f"Email Status    : {email_status_var}\n"
         f"Date_time       : {current_time}")

   with open("reply_output.csv","a",newline="",encoding="UTF-8") as fp:
      writer=csv.writer(fp)
      writer.writerow([Sr_No,frist_name,last_name,company_domain,email_id,email_status_var,current_time])



# # driver_var.quit()

#document.querySelector(".sc-uJMKN.sc-cjHlYL.gvKNbd").textContent