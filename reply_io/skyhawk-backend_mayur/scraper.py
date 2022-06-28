from ast import Try
from functools import cache
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
import tldextract


class scraper():

    def __start(self):
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument(
            '--profile-directory=Profile '+self.CONFIG["profile_id"])

        chromeOptions.add_argument(
            "user-data-dir="+self.CONFIG["user_directory"])
        try:
            self.driver = webdriver.Chrome(
                executable_path=self.CONFIG["driver"],
                options=chromeOptions
            )
            self.driver.maximize_window()
            self.driver.execute_script("window.open('about:blank','_blank');")
            self.action = ActionChains(self.driver)

            self.tabs = {
                'primary': self.driver.current_window_handle,
                'secondary':  self.driver.window_handles[1]
            }

        except Exception as e:
            self.driver = None
            self.tabs = {}
            print("An exception occurred")
            print(e)

    def __init__(self, config):
        self.CONFIG = config
        self.__start()

    def getDriver(self):
        return self.driver

    def goto(self, url, tab):
        if tab in self.tabs:
            self.driver.switch_to.window(self.tabs[tab])
            self.driver.get(url)

    def findElement(self, selector):
        return self.driver.find_element(By.CSS_SELECTOR, selector)

    def switchToFrame(self, frame):
        self.driver.switch_to.frame(frame)

    def clear(self, ele):
        ele.send_keys(Keys.CONTROL + "a")
        ele.send_keys(Keys.DELETE)
        ele.clear()

    def sendKeys(self, ele, key, delay=1):
        self.clear(ele)
        for char in key:
            ele.send_keys(char)
            time.sleep(delay)

    def enter(self, ele):
        ele.send_keys(u'\ue007')

    def submit(self, ele):
        ele.submit()

    def click(self, ele):
        ele.click()

    def getCurrentUrl(self):
        return self.driver.current_url

    def quit(self):
        self.driver.quit()

    def presenceOfElementLocated(self, selector):
        ele = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
        return ele

    def sleep(self, delay):
        #self.driver.implicitly_wait(delay)
        time.sleep(delay)

    def executeScript(self, script):
        return self.driver.execute_script(script)

    def domainName(self,website):
        domainName = tldextract.extract(website).domain + "." + tldextract.extract(website).suffix
        return domainName

    def wholesendKey(self,ele,key):
        ele.send_keys(key)

