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
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=temp")

driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options);
driver.implicitly_wait(30);
driver.get("https://elements.envato.com/sign-in")

while "https://elements.envato.com/sign-in" in driver.current_url:
    time.sleep(3)

driver.get(url)
