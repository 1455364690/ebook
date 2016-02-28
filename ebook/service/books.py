# -*- coding: utf-8 -*-
__author__ = 'yangbo'

from ebook.dao.books import *
from flask import session


class book():
    def __init__(self, title):
        self.title = title
        self.temp = getBook(title)

    def getId(self):
        if self.temp:
            return self.temp[0][0]
        return False

    def getTitle(self):
        if self.temp:
            return self.temp[0][1]
        return False

    def getSrc(self):
        if self.temp:
            return self.temp[0][2]
        return False

    def getImg(self):
        if self.temp:
            return self.temp[0][3]
        return False

    def getBrief(self):
        if self.temp:
            return self.temp[0][4]
        return False

    def getDate(self):
        if self.temp:
            return self.temp[0][5]
        return False

    def getUploader(self):
        if self.temp:
            return self.temp[0][6]
        return False

    def addBook(self, src, img, brief, date, uploader, bigpic):
        if getBook(title=self.title):
            return False
        else:
            addBook(self.title, src, img, brief, date, uploader, bigpic)
            temp = session["username"]
            logtemp = temp+"上传了唱游："+self.title
            actionLog(logtemp)
            return True

    def deletebook(self):
        if deleteBook(self.title):
            temp = session["username"]
            logtemp = temp+"删除了唱游："+self.title
            actionLog(logtemp)
            return True
        return False


