from bs4 import BeautifulSoup

from MyAPI.Article import Article


class ScienceDirect():
    def __init__(self):
        self.volume = ""
        self.issue = ""
        self.year = ""
        self.src = ""
        self.url = ""
        self.articles = []

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
        obj = ScienceDirect()
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
                    obj = ScienceDirect()
                    src = ""
            i+=1

        ScienceDirect.reinit(objs)
        return objs

    def parse(self):
        html = self.src
        date = None
        try:
            volume = html.find("h2", attrs={"class": u"u-text-light u-h1 js-vol-issue"})
            if volume is None:
                volume = html.find("h2", attrs={"class": u"u-text-light u-h1 js-special-issue-title js-title"})
            self.volume = volume.text

            year = html.find("span", attrs={"class": u"js-issue-status text-s"})
            full_date = year.text.split("(")[1].split(")")[0]
            year = year.text.split("(")[1].split(")")[0].split(" ")[1]
            self.year = int(year)
            date = full_date
        except:
            volume = html.find("span", attrs={"class": u"text-s js-vol-issue"})
            self.volume = int(volume.text.split(", ")[0].split("Volume ")[1])
            self.issue = int(volume.text.split("Issue ")[1].split(",")[0])
            self.year = int(volume.text.split("(")[1].split(")")[0])
            date = self.year

        articles = html.find("div", attrs={"class": u"u-padding-top-m u-margin-bottom-xs"})
        articles = articles.find_all("li", attrs={"class": u"js-article-list-item article-item u-padding-top-xs u-margin-bottom-m"})
        for elm in articles:
            article = Article()

            title = elm.find("span", attrs={"class": u"js-article-title"})
            article.title = title.text.replace("\\xe2\\x80\\x98", "'").replace("\\xe2\\x80\\x99", "'").replace("\\xe2\\x80\\x93", "-")

            try:
                authors = elm.find("div", attrs={"class": u"text-s u-clr-grey8 js-article__item__authors"})
                article.authors = authors.text.split(", ")
            except:
                pass

            article.date_published = date

            if article.title != "Editorial Board" and article.title != "Table of contents" and article.title != "Table of Contents":
                self.articles.append(article)

    def print(self):
        print("Volume: " + str(self.volume))
        print("Issue: " + str(self.issue))
        print("Year: " + str(self.year))
        print("Articles:")
        for article in self.articles:
            print(article.title)