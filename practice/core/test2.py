# -*- coding: UTF-8 -*-
# 基础包：生成签名
# author: anqi
import hashlib


def genSign(str):
    """使用md5加密生成签名
    :param str:
    :return: md5加密签名
    """


    m = hashlib.md5()
    b = str.encode(encoding='utf-8')
    m.update(b)

    sign = m.hexdigest()

    return sign.upper()


if __name__ == '__main__':

    str = "isRmbMe=0&passport=17521200974&password=anqi666&secret=92b13c1b3b97492daa47a160cd6086ba"
    sign1 = genSign(str)
    print('"sign"' + ':' + '"' + sign1 + '"')






