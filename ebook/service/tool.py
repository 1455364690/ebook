# encoding=utf8
__author__ = 'yangbo'
import codecs


def encodeChange(path):
    look_gb = codecs.lookup('gbk')
    look_utf = codecs.lookup('utf-8')
    file_old = open(path, 'r')
    fileread = file_old.read()
    gbk_code = fileread.replace('charset=gb2312', 'charset=utf-8')
    tmp = look_gb.decode(gbk_code, 'ignore')[0]
    utf = look_utf.encode(tmp, 'ignore')[0]
    file_old.close()
    f = open(path, 'w')
    f.write(utf)
    f.close()
    return True
