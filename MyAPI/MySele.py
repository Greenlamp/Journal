# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup

class MySele:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_source(self, url):
        self.driver.get(url)
        return BeautifulSoup(self.driver.page_source)