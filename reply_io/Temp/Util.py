import time
from selenium.webdriver.common.by import By

class Util():
    def sendingKeyInput(self,inputSelector,key,delay):
        for word in key:
            inputSelector.send_keys(word)
            time.sleep(delay)


    def waitIfElementPresent(self,driver,element):
        while True:
            try:
                elementStatus=driver.find_element(By.CSS_SELECTOR,element)
            except:
                elementStatus = None

            if elementStatus!=None:
                break
