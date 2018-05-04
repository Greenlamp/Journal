# -*- coding: utf-8 -*-
import urllib

from bs4 import BeautifulSoup


class MyBs:
    def __init__(self):
        self.request_headers = {
            "Accept-Language": "en-US,en;q=0.5",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Referer": "http://thewebsite.com",
            "Connection": "keep-alive"
        }

    def get_source(self, url):
        request = urllib.request.Request(url, headers=self.request_headers)
        contents = urllib.request.urlopen(request).read()
        soup = BeautifulSoup(contents, "html.parser")
        return soup