# -*- coding: utf-8 -*-
__author__ = 'yangbo'

from ebook.service.books import *
from flask import render_template
from json import dumps


@app.route('/')
def index():
    return render_template('index.html')
'''
    接口说明
    该接口返回静态模板文件index.html
'''


@app.route('/data', methods=["POST"])
def getData():
    try:
        result = []
        temp = getBook()
        if temp:
            for i in temp:
                result.append({"id": i[0], "title": i[1], "src": i[2], "img": i[3],
                               "brief": i[4], "date": time.strftime('%Y-%m-%d', time.localtime(i[5])),
                               "uploader": i[6], "bigpic": i[7]})
        return dumps({"code": 0, "data": result, "msg": "ok"})
    except Exception as e:
        exceptionHandler(Exception, e, 1)
        return dumps({"code": 1, "msg": "error"})
'''
    接口说明
    该接口返回首页的数据
    数据为json格式
    ====================
    id: 杂志的id
    title: 杂志的标题
    src: 杂志的地址
    img: 杂志封面图的地址
    brief: 杂志的描述
    date: 杂志上传日期
    uploader: 杂志上传者
    bigpic: 滚播大图的地址
    ====================
'''