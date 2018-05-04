# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
url = "https://www.tandfonline.com/toc/vece20/1/1"
driver.get(url)

assert "The Journal of Economic" in driver.title
"""html= driver.find_element_by_xpath(".//html")
print(html.text)"""

html = driver.page_source
soup = BeautifulSoup(html)
print(soup)
print("\n===============================================\n")

url = "https://www.tandfonline.com/toc/vece20/1/2"
driver.get(url)
assert "The Journal of Economic" in driver.title
html = driver.page_source
soup = BeautifulSoup(html)
print(soup)

driver.close()