# -*- coding: utf-8 -*-
__author__ = 'yangbo'

from ebook.dao.user import *
from flask import session

class user():
    def __init__(self, username, password, email=None, realname=None):
        self.username = username
        self.password = password
        self.email = email
        self.realname = realname
        temp = getUser(username, "byUsername")
        self.state = 0   # default user state 0, the user is not registered
        if temp and temp[0][2] == self.password:
            self.id = temp[0][0]
            self.state = temp[0][4]
            self.lastpost = temp[0][3]

    def isUser(self):
        if self.state >= 1:
            return True
        else:
            return False

    def isNormalUser(self):
        if self.state >= 2:
            return True
        else:
            return False

    def isManager(self):
        if self.state >= 3:
            return True
        else:
            return False

    def isRoot(self):
        if self.state == 4:
            return True
        else:
            return False
    def getId(self):
        if self.isUser():
            return self.id
        return False

    def getUsername(self):
        if self.isUser():
            return self.username
        return False

    def getPassword(self):
        if self.isUser():
            return self.password

    def register(self):
        if self.isUser():
            return False
        elif addUser(self.username, self.password, 1, self.email, self.realname):
            try:
                sendEmail(mail_to_manager, "E刊网用户注册申请", "<h2 align='center'>"+self.realname+
                              "正在注册成为ebook网站用户，点击以下链接去处理</h2>\n"+ "<h3 align='center'>"+
                              "<a href=\"http://ebook.future.org.cn\">"+"E刊网--未来网旗下子网</a></h3>")
                logtemp = self.username+"注册为新用户"
                actionLog(logtemp)
            except Exception as e:
                exceptionHandler(Exception, e, 3)
            finally:
                return True
        else:
            return False

    def addUserByManager(self):
        if self.isUser():
            return False
        elif addUser(self.username, self.password, 1, self.email, self.realname):
            try:
                username = session["username"]
                password = session["password"]
                currentUser = user(username, password)
                if currentUser.isManager():
                    logtemp = "管理员"+username+"添加了新用户："+self.username
                    actionLog(logtemp)
            except Exception as e:
                exceptionHandler(Exception, e, 3)
            finally:
                return True
        else:
            return False

    def changePwd(self, newPass):
        if updateInfo(self.id, newPass, "changePwd"):
            logtemp = self.username+"修改了密码"
            actionLog(logtemp)
            return True
        return False

    def changeUsername(self, username):
        if updateInfo(self.id, username, "changeUsername"):
            logtemp = self.username+"修改了用户名"
            actionLog(logtemp)
            return True
        return False

    def changeEmail(self, email):
        if updateInfo(self.id, email, "changeEmail"):
            logtemp = self.username+"修改了邮箱"
            actionLog(logtemp)
            return True
        return False

    # order = {1:拒绝, 2:认证通过, 3:提升为管理员}
    def authorize(self, uid, order):
        if order:
            username = getUser(uid, "byUsername")[0][1]
            mail_to_user = getUser(uid, "byUsername")[0][5]
            sub = "E刊网通知"
            if order + 1 == 2:
                updateInfo(username, order + 1, "changeState")
                reply = "<h2 align='center'>"+username+"，管理员已通过你的注册申请，快点击以下链接去登陆吧</h2>\n"+ "<h3 align='center'>"+"<a href=\"http://ebook.future.org.cn/\">"+"E刊网--未来网旗下子网</a></h3>"
                sendEmail(mail_to_user, sub, reply)
                logtemp = self.username + "通过了" + username + "的注册请求！"
                actionLog(logtemp)
                return True
            if order + 1 == 3:
                updateInfo(username, order + 1, "changeState")
                reply = "<h2 align='center'>"+username+"，系统已将你设置为管理员，快点击以下链接去查看吧</h2>\n"+ "<h3 align='center'>"+"<a href=\"http://ebook.future.org.cn/\">"+"E刊网--未来网旗下子网</a></h3>"
                sendEmail(mail_to_user, sub, reply)
                logtemp = self.username + "设置" + username + "为管理员！"
                actionLog(logtemp)
                return True
            if order == 3:
                updateInfo(username, order - 1, "changeState")
                reply = "<h2 align='center'>"+username+"，你已被设置为普通用户，如有问题，请咨询E刊网系统管理人员</h2>"
                sendEmail(mail_to_user, sub, reply)
                logtemp = self.username + "设置" + username + "为普通用户！"
                actionLog(logtemp)
                return True
            else:
                return False

    def deleteUser(self, uid):
        if uid == session["id"]:
            return False
        else:
            userObj = getUser(uid, "byId")
            temp = session["username"]
            if deleteUser(uid, "byId"):
                logtemp = temp+"删除了用户:" + userObj[0][1]
                actionLog(logtemp)
                return True



