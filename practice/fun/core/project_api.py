#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json

import common.tools.transfer as transfer
import constants as cs
import core.request as request
import tools.gen_sign as gensign
import tools.time as time
from common.tools import log as log

logging = log.get_log()

headers_oms = {
    "cookie": "JSESSIONID=48F88FA9E1A78067D52B67F2E3654A47; _ga=GA1.2.1000168894.1609123436; _xmLog=h5&8bb38095-bc4f-473b-801a-762ef3edf447&2.2.5; mp_eSpCz4lYpMYgtuhdH0F6Wgtt_mixpanel=%7B%22distinct_id%22%3A%20%22176a73b06d372d-0074a026119f6b-32667006-1aeaa0-176a73b06d4691%22%2C%22_id%22%3A%20%225a5da72e83e7280001435057%22%2C%22email%22%3A%20%22qi.an%40ximalaya.com%22%2C%22lang%22%3A%20%22zh%22%2C%22name%22%3A%20%22%E5%AE%89%E7%90%AA%22%2C%22userKey%22%3A%20%225a5da72e83e7280001435057%22%2C%22%24os_version%22%3A%20%22Macintosh%3B%20Intel%20Mac%20OS%20X%2010_14_6%22%2C%22%24initial_referrer%22%3A%20%22http%3A%2F%2Fteambition.ximalaya.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22teambition.ximalaya.com%22%7D; teambition_private_sid=eyJhdXRoVXBkYXRlZCI6MTYwNjA5NzE4MjQzMiwibG9naW5Gcm9tIjoidGVhbWJpdGlvbiIsInVpZCI6IjVhNWRhNzJlODNlNzI4MDAwMTQzNTA1NyIsInVzZXIiOnsiX2lkIjoiNWE1ZGE3MmU4M2U3MjgwMDAxNDM1MDU3IiwibmFtZSI6IuWuieeQqiIsImVtYWlsIjoicWkuYW5AeGltYWxheWEuY29tIiwiYXZhdGFyVXJsIjoiaHR0cHM6Ly9zdHJpa2VyLnRlYW1iaXRpb24ubmV0L3RodW1ibmFpbC8xMTExNjcxNjI5YmVkNDE5YWUxZWUyYzZlODg4OTQ2M2E4MDMvdy8xMDAvaC8xMDAiLCJyZWdpb24iOiJjbiIsImxhbmciOiIiLCJpc1JvYm90IjpmYWxzZSwib3BlbklkIjoiIiwicGhvbmVGb3JMb2dpbiI6IiJ9fQ==; teambition_private_sid.sig=DtpBLo9eYghey5CE9QRRoe7t8Ds; referral=%7B%22domain%22%3A%22teambition.ximalaya.com%22%2C%22path%22%3A%22%2Flogin%22%2C%22query%22%3A%22%3Fnext_url%3Dhttp%253A%252F%252Fteambition.ximalaya.com%252Fproject%252F5b39ebb6f686d8001909c919%252FsmartGroups%252F%22%2C%22hash%22%3A%22%22%7D; teambition_lang=zh; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; _const_cas_ticket=ad88c684e2ed4629bf61f0fc4b838798; mp_123456_mixpanel=%7B%22distinct_id%22%3A%20%221769925fd8b35a-0cbddd7a0b988a-32667006-1aeaa0-1769925fd8c87d%22%2C%22userKey%22%3A%20%225a5da72e83e7280001435057%22%2C%22created_at%22%3A%20%222018-01-16T07%3A18%3A06.430Z%22%2C%22userLanguage%22%3A%20%22zh%22%2C%22env%22%3A%20%22production%22%2C%22version%22%3A%20%2211.21.3-private.8%22%2C%22daysSinceRegistered%22%3A%201141%2C%22timezone%22%3A%208%2C%22experiments%22%3A%20%5B%5D%2C%22%24os_version%22%3A%20%22Macintosh%3B%20Intel%20Mac%20OS%20X%2010_14_6%22%2C%22%24initial_referrer%22%3A%20%22http%3A%2F%2Fteambition.ximalaya.com%2Flogin%3F%22%2C%22%24initial_referring_domain%22%3A%20%22teambition.ximalaya.com%22%7D; mp_tbpanel__c=0",
    "Content-Type": "application/json;"}

headers_enterprise = {
    "cookie": "JSESSIONID=48F88FA9E1A78067D52B67F2E3654A47; _ga=GA1.2.1000168894.1609123436; _xmLog=h5&8bb38095-bc4f-473b-801a-762ef3edf447&2.2.5; mp_eSpCz4lYpMYgtuhdH0F6Wgtt_mixpanel=%7B%22distinct_id%22%3A%20%22176a73b06d372d-0074a026119f6b-32667006-1aeaa0-176a73b06d4691%22%2C%22_id%22%3A%20%225a5da72e83e7280001435057%22%2C%22email%22%3A%20%22qi.an%40ximalaya.com%22%2C%22lang%22%3A%20%22zh%22%2C%22name%22%3A%20%22%E5%AE%89%E7%90%AA%22%2C%22userKey%22%3A%20%225a5da72e83e7280001435057%22%2C%22%24os_version%22%3A%20%22Macintosh%3B%20Intel%20Mac%20OS%20X%2010_14_6%22%2C%22%24initial_referrer%22%3A%20%22http%3A%2F%2Fteambition.ximalaya.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22teambition.ximalaya.com%22%7D; teambition_private_sid=eyJhdXRoVXBkYXRlZCI6MTYwNjA5NzE4MjQzMiwibG9naW5Gcm9tIjoidGVhbWJpdGlvbiIsInVpZCI6IjVhNWRhNzJlODNlNzI4MDAwMTQzNTA1NyIsInVzZXIiOnsiX2lkIjoiNWE1ZGE3MmU4M2U3MjgwMDAxNDM1MDU3IiwibmFtZSI6IuWuieeQqiIsImVtYWlsIjoicWkuYW5AeGltYWxheWEuY29tIiwiYXZhdGFyVXJsIjoiaHR0cHM6Ly9zdHJpa2VyLnRlYW1iaXRpb24ubmV0L3RodW1ibmFpbC8xMTExNjcxNjI5YmVkNDE5YWUxZWUyYzZlODg4OTQ2M2E4MDMvdy8xMDAvaC8xMDAiLCJyZWdpb24iOiJjbiIsImxhbmciOiIiLCJpc1JvYm90IjpmYWxzZSwib3BlbklkIjoiIiwicGhvbmVGb3JMb2dpbiI6IiJ9fQ==; teambition_private_sid.sig=DtpBLo9eYghey5CE9QRRoe7t8Ds; referral=%7B%22domain%22%3A%22teambition.ximalaya.com%22%2C%22path%22%3A%22%2Flogin%22%2C%22query%22%3A%22%3Fnext_url%3Dhttp%253A%252F%252Fteambition.ximalaya.com%252Fproject%252F5b39ebb6f686d8001909c919%252FsmartGroups%252F%22%2C%22hash%22%3A%22%22%7D; teambition_lang=zh; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; _const_cas_ticket=ad88c684e2ed4629bf61f0fc4b838798; mp_123456_mixpanel=%7B%22distinct_id%22%3A%20%221769925fd8b35a-0cbddd7a0b988a-32667006-1aeaa0-1769925fd8c87d%22%2C%22userKey%22%3A%20%225a5da72e83e7280001435057%22%2C%22created_at%22%3A%20%222018-01-16T07%3A18%3A06.430Z%22%2C%22userLanguage%22%3A%20%22zh%22%2C%22env%22%3A%20%22production%22%2C%22version%22%3A%20%2211.21.3-private.8%22%2C%22daysSinceRegistered%22%3A%201141%2C%22timezone%22%3A%208%2C%22experiments%22%3A%20%5B%5D%2C%22%24os_version%22%3A%20%22Macintosh%3B%20Intel%20Mac%20OS%20X%2010_14_6%22%2C%22%24initial_referrer%22%3A%20%22http%3A%2F%2Fteambition.ximalaya.com%2Flogin%3F%22%2C%22%24initial_referring_domain%22%3A%20%22teambition.ximalaya.com%22%7D; mp_tbpanel__c=0",
    "content - type": "application / x - www - form - urlencoded;charset = UTF - 8"}


# 复制历史项目阶段

def create_project_data():
    res_project_stages = request.api("get", cs.URL_OMS + "/co-oms/api/project/1901/stages", data=None,
                                     headers=headers_oms)
    if res_project_stages:
        # 修改阶段时间戳
        stage_data = res_project_stages['data.yaml']
        # print(stage_data)
        stage_data[0]['beginTime'] = time.gen_stamp_date_today()[0]
        stage_data[0]['endTime'] = time.gen_stamp_date_today()[1]
        # print(stage_data)
        project_content = {"title": cs.TITLE,
                           "subtitle": cs.SUBTITLE,
                           "categoryId": 275,
                           "cover": cs.COVER,
                           "intro": cs.INTRO,
                           "sharePic": cs.SHAREPIC,
                           "cerCover": cs.CERCOVER,
                           "assignType": 1,
                           "completeTaskCount": 1, "stages": stage_data,
                           "enableCer": 1, "enableUserProfit": 1, "enableUserTask": 0,
                           "beginTime": time.gen_stamp_date_today()[0],
                           "endTime": time.gen_stamp_date_today()[1],
                           "status": 1}

        # 新增项目
        # print(project_content)
        res_project_add = request.api("post", cs.URL_OMS + "/co-oms/api/project/add",
                                      json.dumps(project_content), headers=headers_oms)
        # print(res_project_add)
        if res_project_add:
            # 获取项目ID
            project_id = res_project_add['data.yaml']
            # 分配项目给企业
            res_project_dispatch = request.api("post",
                                               cs.URL_OMS + "/co-oms/api/project/" + str(project_id) + "/dispatch",
                                               json.dumps([{"corpId": cs.CORP_ID[0], "totalCount": -1},
                                                           {"corpId": cs.CORP_ID[1], "totalCount": -1}]), headers_oms)
            # print(res_project_dispatch)
            if res_project_dispatch:
                # 登录企业后台
                # login.login_enterprise(cs.PASSPORT, cs.PASSWORD, 0)
                # 企业后台
                # login.login_choose_cope(cs.CORP_ID[0])
                # print(project_id)

                assign_sign = gensign.gen_sign(
                    "curUidCode=_GAQsTvZuwo&projectId=" + str(project_id) + "&uids=" + str(
                        cs.UID[0]) + "&secret=92b13c1b3b97492daa47a160cd6086ba")
                assign_data = {"projectId": project_id,
                               "uids": cs.UID[0],
                               "secretSign": assign_sign}
                # print(assign_data, assign_sign)
                # 企业分配员工
                res_project_assign = request.api("post", cs.URL_ENTERPRISE + "/admin/api/project/target/assign",
                                                 assign_data, headers=headers_enterprise)

                print(project_id)
                # res_delete = request.api("post",
                #                          "http://ops.test.ximalaya.com/co-oms/api/project/" + str(project_id) + "/delete",
                #                          data.yaml=None,
                #                          headers={
                #                              "cookie": "JSESSIONID=D4CB030219E9E2D3404C3BA08E7BC0B3; _ga=GA1.2.2053201037.1604389863; _xmLog=xm_1605252356503_khfxt1g76mniyf; teambition_private_sid=eyJhdXRoVXBkYXRlZCI6MTYwNjA5NzE4MjQzMiwibG9naW5Gcm9tIjoidGVhbWJpdGlvbiIsInVpZCI6IjVhNWRhNzJlODNlNzI4MDAwMTQzNTA1NyIsInVzZXIiOnsiX2lkIjoiNWE1ZGE3MmU4M2U3MjgwMDAxNDM1MDU3IiwibmFtZSI6IuWuieeQqiIsImVtYWlsIjoicWkuYW5AeGltYWxheWEuY29tIiwiYXZhdGFyVXJsIjoiaHR0cHM6Ly9zdHJpa2VyLnRlYW1iaXRpb24ubmV0L3RodW1ibmFpbC8xMTExNjcxNjI5YmVkNDE5YWUxZWUyYzZlODg4OTQ2M2E4MDMvdy8xMDAvaC8xMDAiLCJyZWdpb24iOiJjbiIsImxhbmciOiIiLCJpc1JvYm90IjpmYWxzZSwib3BlbklkIjoiIiwicGhvbmVGb3JMb2dpbiI6IiJ9fQ==; teambition_private_sid.sig=DtpBLo9eYghey5CE9QRRoe7t8Ds; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22175fdfc4c7b67e-02a0e74592ff16-32667006-1764000-175fdfc4c7e9a8%22%2C%22%24device_id%22%3A%22175fdfc4c7b67e-02a0e74592ff16-32667006-1764000-175fdfc4c7e9a8%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; teambition_lang=zh; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; _const_cas_ticket=f268f4a6168c45f59a366fe93431afd8; referral=%7B%22domain%22%3A%22teambition.ximalaya.com%22%2C%22path%22%3A%22%2Fproject%2F5b39ebb6f686d8001909c919%2Fbug%2Fsection%2F5cc66e3d26b9910011315010%2Ftask%2F5fbe0630b3934300130229e5%22%2C%22query%22%3A%22%22%2C%22hash%22%3A%22%22%7D; mp_123456_mixpanel=%7B%22distinct_id%22%3A%20%221758d14f64863d-07ac2649cb174f-32667006-1aeaa0-1758d14f64d72%22%2C%22userKey%22%3A%20%225a5da72e83e7280001435057%22%2C%22created_at%22%3A%20%222018-01-16T07%3A18%3A06.430Z%22%2C%22userLanguage%22%3A%20%22zh%22%2C%22env%22%3A%20%22production%22%2C%22version%22%3A%20%2211.5.6-private.17%22%2C%22daysSinceRegistered%22%3A%201056%2C%22timezone%22%3A%208%2C%22experiments%22%3A%20%5B%5D%2C%22%24os_version%22%3A%20%22Macintosh%3B%20Intel%20Mac%20OS%20X%2010_14_6%22%2C%22%24initial_referrer%22%3A%20%22http%3A%2F%2Fteambition.ximalaya.com%2Flogin%3F%22%2C%22%24initial_referring_domain%22%3A%20%22teambition.ximalaya.com%22%7D; mp_eSpCz4lYpMYgtuhdH0F6Wgtt_mixpanel=%7B%22distinct_id%22%3A%20%221758d167ba793c-09d7e0d85cc06-32667006-1aeaa0-1758d167ba8a9d%22%2C%22_id%22%3A%20%225a5da72e83e7280001435057%22%2C%22email%22%3A%20%22qi.an%40ximalaya.com%22%2C%22lang%22%3A%20%22zh%22%2C%22name%22%3A%20%22%E5%AE%89%E7%90%AA%22%2C%22userKey%22%3A%20%225a5da72e83e7280001435057%22%2C%22%24os_version%22%3A%20%22Macintosh%3B%20Intel%20Mac%20OS%20X%2010_14_6%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; mp_tbpanel__c=0",
                #                              "Content-Type": cs.CONTENT_TYPE})
                # print(res_delete)
                return project_id

def project_user_detail(project_id):
    project_code = transfer.id_to_code(project_id)
    url = cs.URL_MOBILE + "/h5/api/project/v1/" + project_code
    # print(url)
    res = request.api("get", url=url, data=None, headers=cs.headers_mobile)
    return res

def count_total_task(project_id):
    # project_code = transfer.id_to_code(project_id)
    # url = cs.URL_MOBILE + "/h5/api/project/v1/" + project_code
    # # print(url)
    # res = request.api("get", url=url, data.yaml=None, headers=cs.headers_mobile)
    res = project_user_detail(project_id)
    if res:
        # print(res)
        stage = res['data.yaml']['stages']
        # print(stage)
        total_count = 0
        for i in range(0, len(stage)):
            # print(stage[i]['contents'])
            total_count += len(stage[i]['contents'])

        return total_count


if __name__ == '__main__':
    print(count_total_task(1813))
