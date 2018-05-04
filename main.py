# -*- coding: utf-8 -*-
import sys
from dill import dill

from MyAPI.InderScience import InderScience
from MyAPI.MyBs import MyBs
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
    8: 2,
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
        for i in range(0, value):
            url = "https://www.sciencedirect.com/journal/international-review-of-economics-education/vol/{:d}/issue/{:d}".format(key, i+1)
            urls.append(url)

    urls.append("https://www.sciencedirect.com/journal/international-review-of-economics-education/vol/16/part/PA")
    urls.append("https://www.sciencedirect.com/journal/international-review-of-economics-education/vol/16/part/PB")

    return urls

def create_urls_is():
    urls = []

    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2009&vol=1&issue=1/2")
    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2010&vol=1&issue=3")
    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2010&vol=1&issue=4")

    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2011&vol=2&issue=1")
    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2011&vol=2&issue=2")
    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2011&vol=2&issue=3")
    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2011&vol=2&issue=4")

    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2012&vol=3&issue=1")
    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2012&vol=3&issue=2")
    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2012&vol=3&issue=3")
    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2012&vol=3&issue=4")

    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2013&vol=4&issue=1")
    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2013&vol=4&issue=2")
    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2013&vol=4&issue=3")
    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2013&vol=4&issue=4")

    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2014&vol=5&issue=1")
    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2014&vol=5&issue=2")
    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2014&vol=5&issue=3")
    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2014&vol=5&issue=4")

    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2015&vol=6&issue=1")
    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2015&vol=6&issue=2")
    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2015&vol=6&issue=3")
    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2015&vol=6&issue=4")

    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2016&vol=7&issue=1")
    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2016&vol=7&issue=2")
    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2016&vol=7&issue=3")
    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2016&vol=7&issue=4")

    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2017&vol=8&issue=1")
    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2017&vol=8&issue=2")
    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2017&vol=8&issue=3")
    urls.append("http://www.inderscience.com/info/inarticletoc.php?jcode=ijpee&year=2017&vol=8&issue=4")

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

def get_source_is():
    urls = create_urls_is()
    bs = MyBs()
    pages = []
    print("combien ? " + str(len(urls)))
    i=0
    for url in urls:
        print(str(i) + " / " + str(len(urls)))
        source = bs.get_source(url)
        page = InderScience()
        page.src = source
        page.url = url
        pages.append(page)
        i+=1

    InderScience.save(pages, "is.dat")

def tandfonline():
    sys.setrecursionlimit(10000)
    #get_source_tand()
    pages = Tandfonline.load("tand.dat")
    for elm in pages:
        elm.parse()

    return pages

def science_direct():
    sys.setrecursionlimit(10000)
    #get_source_sd()
    pages = ScienceDirect.load("sd.dat")
    for elm in pages:
        elm.parse()

    return pages

def inder_science():
    sys.setrecursionlimit(10000)
    #get_source_is()
    pages = InderScience.load("is.dat")
    for elm in pages:
        elm.parse()

    return pages



def main():
    tand = tandfonline()
    print("TAND DONE")
    sd = science_direct()
    print("SD DONE")
    _is = inder_science()
    print("IS DONE")

    for page in tand:
        page.save_to_csv("JEE.csv")
    for page in sd:
        page.save_to_csv("IREE.csv")
    for page in _is:
        page.save_to_csv("IJPEE.csv")



if __name__ == "__main__":
    main()