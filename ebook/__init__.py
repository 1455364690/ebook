# -*- coding: utf-8 -*-
__author__ = 'yangbo'
from flask import Flask

key = 'nicai'
app = Flask(__name__)
app.secret_key = key


# import controller
import ebook.controller.index
# import ebook.controller.manage
