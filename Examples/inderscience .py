#!/usr/bin/env python
#-*- coding: utf-8 -*-
from lxml import html
from bs4 import BeautifulSoup
import urllib.request

def main():
    url = "http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2011&vol=2&issue=3"
    request_headers = {
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Referer": "http://thewebsite.com",
        "Connection": "keep-alive"
    }

    request = urllib.request.Request(url, headers=request_headers)
    contents = urllib.request.urlopen(request).read()
    soup = BeautifulSoup(contents, "html.parser")
    print(soup)


if __name__ == "__main__":
    main()