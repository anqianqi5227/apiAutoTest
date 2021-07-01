#!/usr/bin/python
# -*- coding: UTF-8 -*-
import constants as cs
import core.request as request
from common import tools as gensign

headers_enterprise = {"cookie":"_xmLog=xm_1604544401291_kh48b3pnpyn5ec; Hm_lvt_53906a063474b0c6164a7a91d073415a=1604544401; "
                            "UM_distinctid=1759732dd05518-04f366bd35f16b-32667006-1aeaa0-1759732dd0759; "
                            "s&e=e40c64c6fa0cd8f566802e4d006c8eb9; UID4=239283; NICKNAME4=qxt-1fr7uh; "
                            "COID=eyJ2ZXIiOiIxLjAifQ.eyJiY0lkIjoxLCJlbnZJZCI6NCwiZXhwIjoxNjA3MTE1NTA0LCJpYXQiOjE2MDcxMTE5MDQsI"
                            "nJtYiI6MCwidWlkIjoyMzkyODN9.6299EF4FEDD5366E8BF80DD8EB3A9AE9A351C69B021206B610D9DCC71A0707A3; "
                            "s&a=%1F__%04TW%1CY%10%0A_%04%0A[%11V@QWSX%06O%07J[U%04V%06%1DZVZCUBVWR@S_O[UB",
                      "content - type": "application / x - www - form - urlencoded;charset = UTF - 8"}

def login_enterprise(passport, password, isRmbMe):

    sign = gensign.gen_sign("isRmbMe="+ str(isRmbMe) +"&passport="+ str(passport) +"&password="+ password +"&secret=92b13c1b3b97492daa47a160cd6086ba")
    url = "https://www.test.qingxuetang.com/admin/api/login/pwd"
    data = {"passport":passport,
           "password":password,
           "isRmbMe":isRmbMe,
           "secretSign":sign}

    res = request.api("post", url, data, headers_enterprise)
    return res

def login_choose_cope(corp_id):

    sign = gensign.gen_sign("code=4e03e5918b5e4b8c8e90f94043f5db7e&corpId=43&secret=92b13c1b3b97492daa47a160cd6086ba")
    url = "https://www.test.qingxuetang.com/admin/api/login/chooseCorp"
    data = {"code":"4e03e5918b5e4b8c8e90f94043f5db7e",
            "corpId":corp_id,
            "secretSign":sign}
    res = request.api("post", url, data, headers_enterprise)
    return res


#def login_mobile(passport, password,)


if __name__ == '__main__':
    # 登录企业后台
    login_enterprise(cs.PASSPORT, cs.PASSWORD, 0)
    # 企业后台
    login_choose_cope(cs.CORP_ID[0])