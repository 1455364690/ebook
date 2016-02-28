# -*- coding: utf-8 -*-
__author__ = 'yangbo'

from ebook.config import *
import MySQLdb
import smtplib
import commands as cmd
from email.mime.text import MIMEText
import time

def connect():
    try:
        conn = MySQLdb.connect(host=mysql_host, user=mysql_user, passwd=mysql_pwd, db=mysql_db, charset="utf8")
    except Exception as e:
        exceptionHandler(Exception, e, 3)
        return False
    else:
        return conn


def execute(sql):
    try:
        conn = connect()
        cur = conn.cursor()
        exe = cur.execute(sql)
        data = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        exceptionHandler(Exception, e, 3)
        return False
    else:
        if data:
            return data
        else:
            return exe


# exception handler


def exceptionHandler(error_type, error, error_level):
    statement = str(error_type) + "=====" + str(error)
    if error_level == 1:
        log.warning(statement)
    elif error_level == 2:
        log.error(statement)
    elif error_level == 3:
        log.critical(statement)
        sendEmail(mail_to_root, "ebook sever call you", cmd.getoutput("tail -n 40" + logfile))
    else:
        return False


# email


def sendEmail(to_user, sub, content):    # toUser 收件人 sub 主题 content 邮件内容
    me = "ebook"+"<"+mail_user+">"
    msg = MIMEText(content, _subtype="html", _charset="utf-8")
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = to_user
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user, mail_pass)
        s.sendmail(me, to_user, msg.as_string())
        s.quit()
    except Exception as e:
        exceptionHandler(Exception, e, 1)
        return False
    finally:
        return True


# write into actionLog


def actionLog(statement):
    if app.debug:
        pass
    else:
        try:
            f = open('log/actionLog', 'a')
            temp = "-----" + time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time())) + "-----" + statement + '\n'
            f.write(str(temp))
        except Exception as e:
            exceptionHandler(Exception, e, 1)
        else:
            f.close()
        finally:
            return True


