#!/usr/bin/python
# -*- coding: UTF-8 -*-
import hashlib


def gen_sign(s):
    m = hashlib.md5()
    m.update(s.encode(encoding='utf-8'))
    sign = m.hexdigest()

    return sign.upper()


def gen_sign_param(param,secret):

    s = ''
    if not isinstance(param, dict):
        dict(param)
    param_list = sorted(param.items(), key=lambda x: x[0])
    for k, val in enumerate(param_list):
        s += str(val[0]) + '=' + str(val[1]) + '&'
    print(s + 'secret' + '=' + secret)
    return gen_sign(s + 'secret' + '=' + secret)


if __name__ == '__main__':
    secret_admin = '92b13c1b3b97492daa47a160cd6086ba'
    secret_h5 = 'f2b0c6a87c560f503b194ffef4c9226f'
    # print(gen_sign("isRmbMe=0&passport=17521200974&password=anqi666&secret=92b13c1b3b97492daa47a160cd6086ba"))
    # print(gen_sign("corpCode=2whCnFfsjzU"))
    # print(gen_sign("code=4e03e5918b5e4b8c8e90f94043f5db7e&corpId=43&secret=92b13c1b3b97492daa47a160cd6086ba"))
    # print((gen_sign("curUidCode=_GAQsTvZuwo&projectId=10165&uids=239283&secret=92b13c1b3b97492daa47a160cd6086ba")))
    # param = {'passport': 17521200974, 'password': 'anqi666', 'isRmbMe': 0}
    # param = {'projectId': 10221,'uids': 239283,'deptIds':'','classIds':''}
    print(gen_sign('curUidCode=_GAQsTvZuwo&projectId=10221&uids=239283&secret=92b13c1b3b97492daa47a160cd6086ba'))
    # print(gen_sign('code=c3a040c464d647b4b385508f427ba548&corpId=43&secret=92b13c1b3b97492daa47a160cd6086ba'))
    # print(gen_sign_param(param,secret_admin))