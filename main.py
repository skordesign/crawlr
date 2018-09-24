from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
import time


#launch url
url = "https://elements.envato.com/stock-video"

# create a new Firefox session
driver = webdriver.Chrome()
driver.implicitly_wait(30);
driver.get("https://elements.envato.com/sign-in")

while driver.current_url == "https://elements.envato.com/sign-in":
    time.sleep(3)

driver.get(url)
