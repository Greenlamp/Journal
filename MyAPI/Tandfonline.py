# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

from MyAPI.Article import Article


class Tandfonline:
    def __init__(self):
        self.volume = ""
        self.issue = ""
        self.year = ""
        self.src = ""
        self.url = ""
        self.articles = []

    def set_src(self, src):
        self.src = src

    @staticmethod
    def reinit(objs):
        for obj in objs:
            obj.volume = ""
            obj.issue = ""
            obj.year = ""

    @staticmethod
    def save(objs, filename):
        with open(filename, 'w') as output:
            for obj in objs:
                print(obj.url)
                output.write(obj.volume)
                output.write("\n")
                output.write(obj.issue)
                output.write("\n")
                output.write(obj.year)
                output.write("\n")
                #output.write(obj.url)
                #output.write("\n")
                output.write(str(obj.src.encode("utf-8")))
                output.write("\n")
                output.write("==[END]==")
                output.write("\n")

    @staticmethod
    def load(filename):
        lines = None
        with open(filename, 'r') as input:
            lines = input.readlines()

        i=0
        objs = []
        obj = Tandfonline()
        src = ""
        for line in lines:
            if i == 0:
                obj.volume = line
            elif i == 1:
                obj.issue = line
            elif i == 2:
                obj.year = line
            #elif i == 3:
            #    obj.url = line
            else:
                if line != "==[END]==\n":
                    src += line
                else:
                    obj.src = BeautifulSoup(src, "lxml")
                    i=0
                    objs.append(obj)
                    obj = Tandfonline()
                    src = ""
            i+=1

        Tandfonline.reinit(objs)
        return objs

    def parse(self):
        html = self.src
        #print(html.prettify())
        volume_year = html.find("div", attrs={"class": u"yearSlider"})
        volume_year = volume_year.find("a", attrs={"class": u"expander open"})
        volume = volume_year.find("span", attrs={"class": u"slider-vol-no"})
        year = volume_year.find("span", attrs={"class": u"slider-vol-year"})
        self.year = int(year.text)
        self.volume = volume.text
        self.issue = int(html.title.text[-1:])
        """issue = issue.find("a", attrs={"class": u"open"})
        print(issue.text)"""
        root = html.find("div", attrs={"class": u"tocContent"})
        articles = root.find_all("table", attrs={"class": u"articleEntry"})

        for elm in articles:
            try:
                article = Article()
                title = elm.find("span", attrs={"class": u"hlFld-Title"})
                article.title = title.text.replace("\\xe2\\x80\\x98", "'")\
                    .replace("\\xe2\\x80\\x99", "'")\
                    .replace("\\xe2\\x80\\x93", "-")\
                    .replace("\\xc2\\xa0", " ")\
                    .replace("\\xe2\\x80\\x9d", '"')\
                    .replace("\\xe2\\x80\\x90", "-")\
                    .replace("\\xe2\\x80\\x94A", "-")\
                    .replace("\\xe2\\x80\\x94", "-")\
                    .replace("\\xc2\\xae", "®")

                authors = elm.find("span", attrs={"class": u"articleEntryAuthorsLinks"})
                authors= authors.find_all("a")
                for author in authors:
                    article.add_author(author.text)

                date_published = elm.find("div", attrs={"class": u"tocEPubDate"})
                date_published = date_published.find("span", attrs={"class": u"maintextleft"})
                date_published = date_published.text.split("Published online: ")[1]
                article.date_published = date_published

                self.articles.append(article)
            except:
                pass

    def print(self):
        print("Volume: " + self.volume)
        print("Issue: " + str(self.issue))
        print("Year: " + str(self.year))
        print("Articles:")
        for article in self.articles:
            print(article.title)

