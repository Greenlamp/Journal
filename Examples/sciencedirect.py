from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
url = "https://www.sciencedirect.com/journal/international-review-of-economics-education/vol/27/suppl/C"
driver.get(url)

assert "International Review" in driver.title
"""html= driver.find_element_by_xpath(".//html")
print(html.text)"""

html = driver.page_source
soup = BeautifulSoup(html)
print(soup)
print("\n===============================================\n")

url = "https://www.sciencedirect.com/journal/international-review-of-economics-education/vol/26/suppl/C"
driver.get(url)
assert "The Journal of Economic" in driver.title
html = driver.page_source
soup = BeautifulSoup(html)
print(soup)

driver.close()