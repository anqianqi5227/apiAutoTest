#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import urllib3

from common.tools import log as log

logging = log.get_log()


def api(method, url, data, headers):
    try:
        global res
        urllib3.disable_warnings()

        if method == "get":
            res = requests.get(url, data, headers=headers)

        if method == "post":
            res = requests.post(url, data, headers=headers)

        # cookies= res.raw.headers.
        response = res.json()
        if response['ret'] != 0:
            logging.info("接口错误：%s %s %s" % (url, response['ret'], response['msg']))
            ex = Exception("ret 非0")
            raise ex

    except Exception as e:

        logging.info("service is error:%s" % e)
        return None
        # print(e)
    else:
        return response
