# -*- coding: UTF-8 -*-
# 基础包：生成签名
# author: anqi
import hashlib


def genSign(passport, password, passportType):
    """使用md5加密生成签名
    :param passport: 账号
    :param password: 密码
    :param passportType: 登录类型
    :return: 加密签名
    """

    str1 = 'passport=' + str(passport) + '&passportType=' + str(passportType) + '&password=' + str(password) + '&secret=f2b0c6a87c560f503b194ffef4c9226f'

    m = hashlib.md5()
    b = str1.encode(encoding='utf-8')
    m.update(b)

    sign = m.hexdigest()


    return sign.upper()


if __name__ == '__main__':
    sign1 = genSign(17521200974, 'anqi666', 1)
    print('"sign"' + ':' + '"' + sign1 + '"')



