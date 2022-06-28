from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import glob
from selenium.webdriver.common.action_chains import ActionChains
import os
from selenium.common.exceptions import TimeoutException
import json
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from linkedin import *

DIR = os.getcwd()
CONFIG = json.load(open(DIR+'/config.json'))

# CHROME = CONFIG['chrome']
# DB = CONFIG['db']
# LINKEDIN_SALES = CONFIG['sales']
# REPLY_IO = CONFIG['reply.io']