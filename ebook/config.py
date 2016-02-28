# -*- coding: utf-8 -*-
__author__ = 'yangbo'
import sys
reload(sys)
sys.setdefaultencoding("utf8")

DEBUG = True

# database
mysql_host = "localhost"
mysql_user = "root"
mysql_pwd = "yangbo"
mysql_db = "ebook"

# logging
import logging as log
from ebook import app

logfile = "log/ebook-log"
# two modes
if not DEBUG:
    log.basicConfig(level=log.INFO,
                    format="%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s",
                    datefmt="%a,%d-%b-%Y@%H:%M:%S",
                    filename=logfile,
                    filemode="a")

# email
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "healthy_kaizhi@163.com"    # 用户名
mail_pass = "qskaizhi123_qaz"   # 口令
mail_to_root = "1299298676@qq.com"
mail_to_manager = "1299298676@qq.com"


# actionLog  这个变量在函数参数列表设置的，这里列出，以作参考
actionLog = 'log/actionLog'
