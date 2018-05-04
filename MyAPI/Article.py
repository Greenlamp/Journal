# -*- coding: utf-8 -*-
class Article:
    def __init__(self):
        self.title = None
        self.authors = []
        self.date_published = None

    def add_author(self, author):
        self.authors.append(author)