# -*- coding: utf-8 -*-
__author__ = 'yangbo'
import sys
reload(sys)
sys.setdefaultencoding("utf8")
from ebook.service.user import *
from ebook.service.books import *
from ebook.service.tool import encodeChange
from ebook.dao.base import *
from ebook.controller.auth import requires_auth
from werkzeug.utils import secure_filename
from flask import render_template, request, session
from hashlib import md5
import zipfile


@app.route('/register', methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]
    pwd = md5(password).hexdigest()
    email = request.form["email"]
    realname = request.form["realname"]
    userObj = user(username, pwd, email=email, realname=realname)
    userObj.register()
    return 'success'


@app.route('/addUser', methods=["POST"])
@requires_auth
def addUser():
    username = request.form["username"]
    password = request.form["password"]
    pwd = md5(password).hexdigest()
    email = request.form["email"]
    realname = request.form["realname"]
    userObj = user(username, pwd, email=email, realname=realname)
    userObj.addUserByManager()
    return 'success'


@app.route('/login', methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    pwd = md5(password).hexdigest()
    userObj = user(username, pwd)
    if userObj.isNormalUser():
        session["id"] = userObj.id
        session["state"] = userObj.state
        session["username"] = username
        session["password"] = pwd
        session["lastpost"] = userObj.lastpost
        updateInfo(username, int(time.time()), "changeLastLogin")
        logtemp = username+"登陆成功！"
        actionLog(logtemp)
        return 'success'
    else:
        return 'failed'


@app.route('/logout', methods=["POST"])
@requires_auth
def logout():
    try:
        username = session["username"]
        session.pop('id', None)
        session.pop('username', None)
        logtemp = username + "注销登陆！"
        actionLog(logtemp)
        return 'success'
    except Exception as e:
        exceptionHandler(Exception, e, 1)
        return 'failed'


@app.route('/changepsw', methods=["POST"])
@requires_auth
def changepsw():
    username = session["username"]
    oldpassword = request.form["oldPassword"]
    password = md5(oldpassword).hexdigest()
    userObj = user(username, password)
    if userObj.isNormalUser():
        newpassword = request.form["newPassword"]
        userObj.changePwd(md5(newpassword).hexdigest())
        return 'success'
    else:
        return 'failed'


@app.route('/changeUserData', methods=["POST"])
@requires_auth
def changeUserData():
    username = session["username"]
    password = session["password"]
    userObj = user(username, password)
    if userObj.isNormalUser():
        newusername = request.form["newUsername"]
        newEmail = request.form["newEmail"]
        userObj.changeUsername(newusername)
        userObj.changeEmail(newEmail)
        return 'success'
    else:
        return 'failed'


@app.route('/changestate', methods=["POST"])
@requires_auth
def changestate():
    username = session["username"]
    password = session["password"]
    userObj = user(username, password)
    if userObj.isManager():
        user_to_change = request.form["username"]
        state = request.form["state"]
        userObj.authorize(user_to_change, int(state))
        return 'success'
    else:
        return 'failed'


@app.route('/deleteUser', methods=["POST"])
@requires_auth
def deleteuser():
    username = session["username"]
    password = session["password"]
    user_to_delete = request.form["userid"]
    userObj = user(username, password)
    if userObj.isManager() and userObj.deleteUser(int(user_to_delete)):
        return 'success'
    else:
        return 'failed'


@app.route('/getUser', methods=["POST"])
@requires_auth
def getUser():
    try:
        username = session["username"]
        password = session["password"]
        userObj = user(username, password)
        result = {"id": userObj.id, "username": userObj.username, "lastpost": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(session["lastpost"])), "state": userObj.state,
                  "email": userObj.email, "realname": userObj.realname}
        from json import dumps
        return dumps(result)
    except Exception as e:
        exceptionHandler(Exception, e, 1)
        return 'failed'


@app.route('/getUserList', methods=["POST"])
@requires_auth
def getUserList():
    try:
        temp = getAllUsers()
        result = []
        for i in temp:
            result.append({"id": i[0], "username": i[1], "lastpost": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i[3])), "state": i[4],
                           "email": i[5], "realname": i[6]})
        from json import dumps
        tem = {"state": session["state"], "user": result}
        return dumps(tem)
    except Exception as e:
        exceptionHandler(Exception, e, 1)
        return 'failed'


@app.route('/uploader', methods=["POST"])
@requires_auth
def upload():
    title = request.form['title']
    brief = request.form['brief']
    dliver = session['username']
    zip_file = request.files['zipfile']
    cover = request.files['cover']
    bigpic = request.files['bigpic']
    bookObj = getBook(title)
    if not bookObj:
        if zip_file.filename.endswith('.zip'):
            location = 'ebook/static/src/'+time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))+'.zip'
            zip_file.save(location)

            f = zipfile.ZipFile(location, 'r')
            outpath = "ebook/static/www/"+time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            for i in f.namelist():
                f.extract(i, outpath)
            f.close()

            base = outpath[6:]+'/'+secure_filename((f.namelist())[0]).encode('utf8')
            src = base + '/online.htm'

            import os
            path = os.path.abspath('.') + '/ebook/' + src
            encodeChange(path)

            covername = secure_filename(cover.filename).lower()
            picname = secure_filename(bigpic.filename).lower()
            if covername.endswith('.jpg') or covername.endswith('.png'):
                address = "ebook/static/src/cover/"+md5(covername + str(time.time())).hexdigest()[0:20] + '.' + covername.split('.')[-1]
                cover.save(address)
                img = address[6:]
                if picname.endswith('.jpg') or picname.endswith('.png'):
                    address2 = "ebook/static/src/bigpic/"+md5(picname + str(time.time())).hexdigest()[0:20] + '.' + picname.split('.')[-1]
                    bigpic.save(address2)
                    bigpicsrc = address2[6:]
                    date = int(time.time())
                    bookObj = book(title)
                    bookObj.addBook(src, img, brief, date, dliver, bigpicsrc)
                    return render_template("upload.html")
                else:
                    return '请按要求提供轮播配图，然后重新上传！'
            else:
                return '请按要求提供封面图，然后重新上传！'
        else:
            return '请按要求上传文件！'
    else:
        return '文件名已存在！'


@app.route('/updatebook', methods=["POST"])
@requires_auth
def updatebook():
    username = session["username"]
    password = session["password"]
    bookid = request.form["id"]
    title = request.form["title"]
    brief = request.form["brief"]
    userObj = user(username, password)
    if userObj.isNormalUser() and updateBook(title, brief, bookid):
        return 'success'
    else:
        return 'failed'


@app.route('/bookDelete', methods=["POST"])
@requires_auth
def bookDelete():
    username = session["username"]
    password = session["password"]
    booktitle = request.form["booktitle"]
    userObj = user(username, password)
    bookObj = book(booktitle)
    if userObj.isNormalUser() and bookObj.deletebook():
        return 'success'
    else:
        return 'failed'


@app.route('/firstToKnow', methods=["GET"])
@requires_auth
def firstToKnow():
    return render_template('firstToKnow.html')


@app.route('/userList', methods=["GET"])
@requires_auth
def userList():
    return render_template('user.html')


@app.route('/bookList', methods=["GET"])
@requires_auth
def bookList():
    return render_template('upload.html')


@app.route('/getBook', methods=["POST"])
@requires_auth
def getbook():
    bookid = request.form["bookid"]
    bookObj = getBook(int(bookid))
    result = []
    if bookObj:
        result.append({"id": bookObj[0][0], "title": bookObj[0][1], "src": bookObj[0][2], "img": bookObj[0][3],
                           "brief": bookObj[0][4], "date": time.strftime('%Y-%m-%d', time.localtime(bookObj[0][5])),
                           "uploader": bookObj[0][6], "bigpic": bookObj[0][7]})
        from json import dumps
        return dumps(result)
    else:
        return 'failed'


@app.route('/getBookList', methods=["POST"])
@requires_auth
def getBookList():
    try:
        result = []
        temp = getBook()
        if temp:
            for i in temp:
                result.append({"id": i[0], "title": i[1], "src": i[2], "img": i[3],
                           "brief": i[4], "date": time.strftime('%Y-%m-%d', time.localtime(i[5])),
                           "uploader": i[6], "bigpic": i[7]})
        from json import dumps
        return dumps(result)
    except Exception as e:
        exceptionHandler(Exception, e, 1)
        return '0'
