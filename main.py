# -*- coding: utf-8 -*-
import sys
from dill import dill

from MyAPI.MySele import MySele
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


def create_urls_tand():
    urls = []
    for key, value in tand.items():
        base_url = "https://www.tandfonline.com/toc/vece20/"
        for i in range(0, value):
            url = base_url + str(key) + "/" + str(i+1)
            urls.append(url)

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




def main():
    sys.setrecursionlimit(10000)
    #get_source_tand()
    pages = Tandfonline.load("tand.dat")
    print(pages)




if __name__ == "__main__":
    main()