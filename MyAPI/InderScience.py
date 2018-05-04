from bs4 import BeautifulSoup

from MyAPI.Article import Article


class InderScience():
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
        obj = InderScience()
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
                    obj = InderScience()
                    src = ""
            i+=1

            InderScience.reinit(objs)
        return objs

    def parse(self):
        html = self.src
        title = html.find("h2", attrs={"align": u"center"})
        year = title.text.split(" ")[0]
        volume = title.text.split("Vol. ")[1].split(" ")[0]
        issue = title.text.split("No. ")[1]

        self.year = year
        self.volume = volume
        self.issue = issue

        root = title.findNext("table").findNext("table")
        articles = root.find_all("tr")
        for elm in articles:
            td = elm.find("td", attrs={"colspan": u"2"})
            if td is not None:
                article = Article()
                title = td.find("a")
                article.add_title(title.text)
                test = td.find_all("br")
                br = test[0]
                authors = br.nextSibling
                article.authors = authors.split(", ")
                article.date_published = self.year

                self.articles.append(article)




    def print(self):
        print("Volume: " + str(self.volume))
        print("Issue: " + str(self.issue))
        print("Year: " + str(self.year))
        print("Articles:")
        for article in self.articles:
            print(article.title)

    def save_to_csv(self, filename):
        with open(filename, 'a') as output:
            for article in self.articles:
                output.write("IJPEE")
                output.write(";")
                output.write(self.volume)
                output.write(";")
                output.write(str(self.year))
                output.write(";")
                output.write(str(self.issue))
                output.write(";")
                output.write(article.title)
                output.write(";")
                output.write(article.get_authors())
                output.write("\n")