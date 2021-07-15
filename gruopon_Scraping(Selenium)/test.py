import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome(r"C:\Users\116\.wdm\drivers\chromedriver\win32\90.0.4430.24\chromedriver.exe")
driver.get("https://docs.microsoft.com/en-us/graph/tutorials/javascript")
time.sleep(3)
driver.get("https://www.guru.com/")
time.sleep(3)
driver.get("https://translate.google.com/?source=gtx&sl=en&tl=ko&op=translate")