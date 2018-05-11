# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver

"""driver = webdriver.Chrome()
url = "https://www.wakfu.com/fr/mmorpg/encyclopedie/armures?size=24&page=1"

driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html)
print(soup)
print("\n===============================================\n")

url = "https://www.wakfu.com/fr/mmorpg/encyclopedie/armures?size=24&page=2"
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html)
print(soup)

driver.close()
"""

def main():
    driver = webdriver.Chrome()
    for i in range(0, 191):
        url = "https://www.wakfu.com/fr/mmorpg/encyclopedie/armures?size=24&page={:d}".format(i+1)
        src = get_source(driver, url)
        filename = "./source/{:d}.html".format(i+1)
        write_in_file(filename, src)
    driver.close()

def write_in_file(filename, src):
        with open(filename, 'wb') as output:
            output.write(src)

def get_source(driver, url):
    driver.get(url)
    html = driver.page_source
    return str.encode(html)

main()