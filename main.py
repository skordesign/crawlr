from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os


#launch url
loginPath = "https://elements.envato.com/sign-in"
url = "https://elements.envato.com/stock-video"

# create a new Firefox session
driver = webdriver.Chrome()
driver.implicitly_wait(30);
driver.get(loginPath)


driver.implicitly_wait(30);
driver.get(url)
