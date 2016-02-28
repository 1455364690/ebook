# -*- coding: utf-8 -*-
__author__ = 'yangbo'

from ebook.dao.base import *


def addUser(username, password, state, email, realname):
    sql = """insert into user (username, password, state, email, realname) values("{}","{}","{}","{}","{}")""".\
        format(username, password, state, email, realname)
    return execute(sql)


def getUser(data, dataType):
    dt_dict = {"byUsername": "username", "byId": "id", "byState": "state"}
    if dataType not in dt_dict:
        return False
    else:
        sql = """select * from user where {} = '{}'""".format(dt_dict[dataType], data)
    return execute(sql)


def getAllUsers():
    sql = """select * from user order by state desc"""
    return execute(sql)


def deleteUser(data, dataType):
    dt_dict = {"byUsername": "username", "byId": "id"}
    if dataType not in dt_dict:
        return False
    else:
        sql = """delete from user where {} = '{}'""".format(dt_dict[dataType], data)
    return execute(sql)


def updateInfo(username, data, dataType):
    dt_dict = {"changeUsername": "username", "changePwd": "password",
               "changeLastLogin": "lastpost", "changeState": "state", "changeEmail": 'email'}
    if dataType not in dt_dict:
        return False
    else:
        sql = """update user set {} = '{}' where username = '{}'""".format(dt_dict[dataType], data, username)
    return execute(sql)