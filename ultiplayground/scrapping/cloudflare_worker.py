import os

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "/usr/bin/google-chrome-beta"
options.add_argument("--headless")

driver = webdriver.Chrome(f"{os.getcwd()}/chromedriver", options=options)
driver.get("https://developers.cloudflare.com/workers")

html = driver.page_source

driver.close()

soup = BeautifulSoup(html, "html.parser")

print(soup)
