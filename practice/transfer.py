#!/usr/bin/python
# -*- coding: UTF-8 -*-


# import core.request as request
import


def id_to_code(id):

    data = {"serverName": "id-encode",
            "params": "long:"+str(id)}
    res = request.api("post", url=cs.URL_OMS+"/co-oms/api/hook/invoke", data=data, headers=None)
    return res['data.yaml']

def code_to_id(code):

    data = {"serverName": "id-decode",
            "params": "long:"+code}
    res = request.api("post", url=cs.URL_OMS+"/co-oms/api/hook/invoke", data=data, headers=None)
    return res['data.yaml']

if __name__ == '__main__':
    print(id_to_code(1189))
    print(code_to_id("VhvWOAS_0io"))