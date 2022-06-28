# Import the required modules
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import json
import pyautogui
pyautogui.FAILSAFE= True
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




def guiClick(x,y):
    pyautogui.click(x,y)

def hover(x,y):
    pyautogui.moveTo(x,y)

def rightClick():
    pyautogui.click(button='right')

def refresh():
    pyautogui.hotkey('ctrl', 'r')

def copy():
    pyautogui.hotkey('ctrl', 'c')

def clear():
    pyautogui.hotkey("backspace")

def paste():
    pyautogui.hotkey('ctrl', 'v')


def write(key):
    pyautogui.write(key)

def page_is_loading(driver0bj):
    timeout = time.time() + 60 * 1
    while True:
        x = driver0bj.execute_script("return document.readyState")
        # print(f"page_status : {x}")
        if x == "complete" or time.time() > timeout :
            return True
        else:
            yield False




#===================================chrome_har_downloder

def chromeDriver():

    driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
    driver.maximize_window()

    driver.get("https://www.flipkart.com/")

    pyautogui.hotkey('ctrl','shift', 'i')
    time.sleep(2)
    pyautogui.hotkey('ctrl','shift', 'p')
    time.sleep(1)
    pyautogui.typewrite("network")
    time.sleep(1)
    pyautogui.press("enter")

    # driver.refresh()

    # while not page_is_loading(driver):
    #     continue


    # hover(1831,485)
    # rightClick()
    # time.sleep(5)
    #
    # saveHarlocation = pyautogui.locateOnScreen('saveHarChrome_Edge.png',confidence=0.6)
    # saveHarpoint = pyautogui.center(saveHarlocation)
    # guiClick(saveHarpoint.x,saveHarpoint.y)
    # time.sleep(2)
    # copy()
    # time.sleep(1)
    #
    # fileName = str(pyperclip.paste()).replace(".har","_Chrome.har")
    #
    # time.sleep(5)
    # clear()
    # time.sleep(1)
    #
    # # print(fileName)
    # write(fileName)
    # time.sleep(3)
    # pyautogui.press("Enter")
    # print("enter")
    #
    # time.sleep(2)
    #
    driver.close()



# ============================================================================================================

#
#
def firefoxDriver():
    driver = webdriver.Firefox(executable_path="drivers/geckodriver.exe")
    driver.maximize_window()
    driver.get("https://www.flipkart.com/")

    while not page_is_loading(driver):
        continue
    #
    time.sleep(2)
    pyautogui.hotkey('ctrl','shift', 'e')
    time.sleep(5)
    # driver.refresh()
    #
    # while not page_is_loading(driver):
    #     continue
    #
    # time.sleep(2)
    # hover(1844, 831)
    # time.sleep(1)
    # rightClick()
    # time.sleep(5)
    #
    #
    # saveHarlocation = pyautogui.locateOnScreen('saveHarFirefox.png',confidence=0.6)
    # saveHarpoint = pyautogui.center(saveHarlocation)
    # guiClick(saveHarpoint.x,saveHarpoint.y)
    # time.sleep(2)
    # copy()
    # time.sleep(1)
    #
    # fileName = str(pyperclip.paste()).replace(".har","_Firefox.har")
    #
    # time.sleep(5)
    # clear()
    # time.sleep(1)
    #
    # # print(fileName)
    # write(fileName)
    # time.sleep(3)
    # pyautogui.press("Enter")
    # print("enter")
    #
    # time.sleep(2)
    #
    driver.close()


#===================================================================================================

def edgeDriver():

    driver = webdriver.Edge(executable_path="drivers/msedgedriver.exe")
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    pyautogui.hotkey('ctrl','shift', 'i')
    time.sleep(2)
    pyautogui.hotkey('ctrl','shift', 'p')
    time.sleep(1)
    pyautogui.typewrite("network")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(2)
    # driver.refresh()
    #
    # while not page_is_loading(driver):
    #     continue
    #
    #
    # hover(1869,461)
    # rightClick()
    # time.sleep(5)
    #
    # saveHarlocation = pyautogui.locateOnScreen('saveHarChrome_Edge.png',confidence=0.6)
    # saveHarpoint = pyautogui.center(saveHarlocation)
    # guiClick(saveHarpoint.x,saveHarpoint.y)
    # time.sleep(2)
    # copy()
    # time.sleep(1)
    #
    # fileName = str(pyperclip.paste()).replace(".har","_Edge.har")
    #
    # time.sleep(5)
    # clear()
    # time.sleep(1)
    #
    # # print(fileName)
    # write(fileName)
    # time.sleep(3)
    # pyautogui.press("Enter")
    # print("enter")
    #
    # time.sleep(2)

    driver.close()


urls =['https://www.flipkart.com/']

for url in urls:
     print(url)

