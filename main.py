# -*- coding: utf-8 -*-
import sys
from dill import dill

from MyAPI.MySele import MySele
from MyAPI.ScienceDirect import ScienceDirect
from MyAPI.Tandfonline import Tandfonline

tand = {
    40: 4,
    41: 4,
    42: 4,
    43: 4,
    44: 4,
    45: 4,
    46: 4,
    47: 4,
    48: 4,
    49: 2
}

sd = {
    9: 2,
    10: 2,
    11: 2,
    12: 1,
    13: 1,
    14: 1,
    15: 1,
    17: 1,
    18: 1,
    19: 1,
    20: 1,
    21: 1,
    22: 1,
    23: 1,
    24: 1,
    25: 1,
    26: 1,
    27: 1
}


def create_urls_tand():
    urls = []
    for key, value in tand.items():
        base_url = "https://www.tandfonline.com/toc/vece20/"
        for i in range(0, value):
            url = base_url + str(key) + "/" + str(i+1)
            urls.append(url)

    return urls

def create_urls_sd():
    urls = []
    for key, value in sd.items():
        url = "https://www.sciencedirect.com/journal/international-review-of-economics-education/vol/{:d}/issue/{:d}".format(key, value)
        urls.append(url)

    urls.append("https://www.sciencedirect.com/journal/international-review-of-economics-education/vol/16/part/PA")
    urls.append("https://www.sciencedirect.com/journal/international-review-of-economics-education/vol/16/part/PB")

    print(urls)

    return urls

def get_source_tand():
    urls = create_urls_tand()
    sele = MySele()
    pages = []
    for url in urls:
        source = sele.get_source(url)
        page = Tandfonline()
        page.set_src(source)
        page.url = url
        pages.append(page)

    Tandfonline.save(pages, "tand.dat")

def get_source_sd():
    urls = create_urls_sd()
    sele = MySele()
    pages = []
    for url in urls:
        source = sele.get_source(url)
        page = ScienceDirect()
        page.src = source
        page.url = url
        pages.append(page)

    ScienceDirect.save(pages, "sd.dat")

def tandfonline():
    sys.setrecursionlimit(10000)
    #get_source_tand()
    pages = Tandfonline.load("tand.dat")
    for elm in pages:
        elm.parse()
        elm.print()
        print("===================================")

def science_direct():
    sys.setrecursionlimit(10000)
    #get_source_sd()
    pages = ScienceDirect.load("sd.dat")
    for elm in pages:
    #elm = pages[0]
        elm.parse()
        elm.print()
        print("===================================")



def main():
    tandfonline()
    #science_direct()



if __name__ == "__main__":
    main()