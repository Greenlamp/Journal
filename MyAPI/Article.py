# -*- coding: utf-8 -*-
class Article:
    def __init__(self):
        self.title = None
        self.authors = []
        self.date_published = None

    def add_author(self, author):
        author = self.treatment(author)
        self.authors.append(author)

    def add_title(self, title):
        title = self.treatment(title)
        self.title = title

    def treatment(self, sent):
        return sent.replace("\\xe2\\x80\\x98", "'")\
            .replace("\\xe2\\x80\\x99", "'")\
            .replace("\\xe2\\x80\\x93", "-")\
            .replace("\\xc2\\xa0", " ")\
            .replace("\\xe2\\x80\\x9d", '"')\
            .replace("\\xe2\\x80\\x90", "-")\
            .replace("\\xe2\\x80\\x94A", "-")\
            .replace("\\xe2\\x80\\x94", "-")\
            .replace("\\xc2\\xae", "®")\
            .replace("\\xc3\\xb6", "ö") \
            .replace("\\xc3\\xa9", "é") \
            .replace("\\xc3\\xa4", "ä") \
            .replace("\\xc5\\xa1", "š") \
            .replace("\\xc3\\xa1", "á") \
            .replace("\\xc3\\xa", "à") \
            .replace("\\xe2\\x80\\x99", "'") \
            .replace("\\xc3\\xb8", "ø") \
            .replace("\\'", "'")\
            .replace("\\xe2\\x80\\x98", "'")\
            .replace("\\xe2\\x80\\x99", "'")\
            .replace("\\xe2\\x80\\x93", "-")

    def get_authors(self):
        return ", ".join(self.authors)