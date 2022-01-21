import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pickle

url = ""

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
webdriver_service = Service("/home/nari/dev/scraper/chromedriver")

browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

browser.get(url)
browser.refresh()
username = browser.find_element(By.ID,"secretLogin")
password= browser.find_element(By.ID,"secretPassword")
time.sleep(5)

username.send_keys("")
password.send_keys("")

cookies = browser.find_element(By.ID,"confirm-cookies").click()
login = browser.find_element(By.ID,"secretSubmit").click()

pickle.dump( browser.get_cookies() , open("cookies.pkl","wb"))

currntV = browser.find_element(By.CLASS_NAME,"current").get_attribute("innerHTML")
print(currntV)

findlatest512 = browser.find_element(By.XPATH("a[contains(text(),'512x')]"))
print(findlatest512)