# -*- coding: utf-8 -*-
__author__ = 'yangbo'

from ebook.dao.base import *
from flask import session

def addBook(title, src, img, brief, date, uploader, bigpic):
    sql = """insert into books (title, src, img, brief, date, uploader, bigpic) values("{}","{}","{}","{}","{}","{}","{}")""".\
        format(title, src, img, brief, date, uploader, bigpic)
    return execute(sql)


def getBook(id=None, title=None):
    if id:
        sql = """select * from books where id = '{}'""".format(id)
    elif title:
        sql = """select * from books where title = '{}'""".format(title)
    else:
        sql = """select * from books order by id DESC """
    return execute(sql)


def updateBook(title, brief, bookid):
    sql = """update books set title = '{}', brief = '{}' where id='{}'""".format(title, brief, bookid)
    tem = execute(sql)
    if tem:
        temp = session["username"]
        logtemp = temp+"修改了了唱游的信息："+title
        actionLog(logtemp)
    return tem


def deleteBook(title):
    sql = """delete from books where title = '{}'""".format(title)
    if execute(sql):
        return True
    else:
        return False
