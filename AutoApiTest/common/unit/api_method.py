#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import urllib3
import os, random
from common.tools import log as log
from requests_toolbelt import MultipartEncoder
from common.config_module.config_read import Config
from Main import root_path

logging = log.get_log()


def post(url, request_parameter_type, headers, timeout=8, data=None, files=None, cookie=None):
    # global response
    """

    :param url: 请求地址
    :param request_parameter_type: 请求参数格式（form_data,raw）
    :param headers: 请求头
    :param timeout: 超时时间
    :param data: 请求参数
    :param files: 文件路径(list)
    :param cookie: cookie
    :return:
    """
    urllib3.disable_warnings()
    if 'form_data' in request_parameter_type:
        for i in range(len(files)):
            # value = files[i]
            if '/' in files[i]:
                files[i] = (os.path.basename(files[i]), open(files[i], 'rb'))
        enc = MultipartEncoder(
            fields=files,
            boundary='-----' + str(random.randint(1e28, 1e29 - 1))
        )

        response = requests.post(url=url, data=enc, headers=headers, timeout=timeout, cookies=cookie)

    elif 'data' in request_parameter_type:
        response = requests.post(url=url, data=data, headers=headers, timeout=timeout, cookies=cookie)

    elif 'json' in request_parameter_type:
        response = requests.post(url=url, json=data, headers=headers, timeout=timeout, cookies=cookie)

    try:
        if response.status_code != 200:
            return response.status_code, response.text
        else:
            return response.status_code, response.json()

    except Exception as e:
        logging.error(e, exc_info=True)
        raise


def get(url, data, headers, timeout=8, cookie=None):
    """

    :param url: 请求地址
    :param data: 请求参数
    :param headers: 请求头
    :param timeout: 超时时间
    :param cookie: cookie
    :return:
    """
    response = requests.get(url=url, data=data, headers=headers, timeout=timeout, cookies=cookie)
    if response.status_code == 301:
        response = requests.get(url=response.headers['location'])

    try:
        if response.status_code != 200:
            return response.status_code, response.text
        else:
            return response.status_code, response.json()

    except Exception as e:
        logging.error(e)
        raise


def save_cookie(url, request_parameter_type, headers, timeout=8, data=None, files=None, cookie=None):
    cookie_path = root_path + '/common/config_module/relevance/cookie.ini'
    if 'form_data' in request_parameter_type:
        for i in range(len(files)):
            # value = files[i]
            if '/' in files[i]:
                files[i] = (os.path.basename(files[i]), open(files[i], 'rb'))
        enc = MultipartEncoder(
            fields=files,
            boundary='-----' + str(random.randint(1e28, 1e29 - 1))
        )

        response = requests.post(url=url, data=enc, headers=headers, timeout=timeout, cookies=cookie)
        print(response.json())
    elif 'data' in request_parameter_type:
        response = requests.post(url=url, data=data, headers=headers, timeout=timeout, cookies=cookie)

    elif 'json' in request_parameter_type:
        response = requests.post(url=url, json=data, headers=headers, timeout=timeout, cookies=cookie)
    try:
        c = ''
        if response.status_code != 200:
            return response.status_code, response.text
        else:
            cookie = response.cookies.get_dict()
            for i in cookie:
                c += c + (i + '=' + cookie[i]) + ';'
            cf = Config(cookie_path)
            cf.add_section_option('cookie', 'cookie', c)
        return response.status_code, response.json()
    except Exception as e:
        logging.exception('ERROR')
        logging.error(e)
        raise
        # if __name__ == '__main__':
        #     url = 'http://"http://ops.test.ximalaya.com"/co-oms/api/project/add'
        #     headers = {'cookie': 'JSESSIONID=48F88FA9E1A78067D52B67F2E3654A47; _ga=GA1.2.1000168894.1609123436; _xmLog=h5&8bb38095-bc4f-473b-801a-762ef3edf447&2.2.5; mp_eSpCz4lYpMYgtuhdH0F6Wgtt_mixpanel=%7B%22distinct_id%22%3A%20%22176a73b06d372d-0074a026119f6b-32667006-1aeaa0-176a73b06d4691%22%2C%22_id%22%3A%20%225a5da72e83e7280001435057%22%2C%22email%22%3A%20%22qi.an%40ximalaya.com%22%2C%22lang%22%3A%20%22zh%22%2C%22name%22%3A%20%22%E5%AE%89%E7%90%AA%22%2C%22userKey%22%3A%20%225a5da72e83e7280001435057%22%2C%22%24os_version%22%3A%20%22Macintosh%3B%20Intel%20Mac%20OS%20X%2010_14_6%22%2C%22%24initial_referrer%22%3A%20%22http%3A%2F%2Fteambition.ximalaya.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22teambition.ximalaya.com%22%7D; teambition_private_sid=eyJhdXRoVXBkYXRlZCI6MTYwNjA5NzE4MjQzMiwibG9naW5Gcm9tIjoidGVhbWJpdGlvbiIsInVpZCI6IjVhNWRhNzJlODNlNzI4MDAwMTQzNTA1NyIsInVzZXIiOnsiX2lkIjoiNWE1ZGE3MmU4M2U3MjgwMDAxNDM1MDU3IiwibmFtZSI6IuWuieeQqiIsImVtYWlsIjoicWkuYW5AeGltYWxheWEuY29tIiwiYXZhdGFyVXJsIjoiaHR0cHM6Ly9zdHJpa2VyLnRlYW1iaXRpb24ubmV0L3RodW1ibmFpbC8xMTExNjcxNjI5YmVkNDE5YWUxZWUyYzZlODg4OTQ2M2E4MDMvdy8xMDAvaC8xMDAiLCJyZWdpb24iOiJjbiIsImxhbmciOiIiLCJpc1JvYm90IjpmYWxzZSwib3BlbklkIjoiIiwicGhvbmVGb3JMb2dpbiI6IiJ9fQ==; teambition_private_sid.sig=DtpBLo9eYghey5CE9QRRoe7t8Ds; referral=%7B%22domain%22%3A%22teambition.ximalaya.com%22%2C%22path%22%3A%22%2Flogin%22%2C%22query%22%3A%22%3Fnext_url%3Dhttp%253A%252F%252Fteambition.ximalaya.com%252Fproject%252F5b39ebb6f686d8001909c919%252FsmartGroups%252F%22%2C%22hash%22%3A%22%22%7D; teambition_lang=zh; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; _const_cas_ticket=ad88c684e2ed4629bf61f0fc4b838798; mp_123456_mixpanel=%7B%22distinct_id%22%3A%20%221769925fd8b35a-0cbddd7a0b988a-32667006-1aeaa0-1769925fd8c87d%22%2C%22userKey%22%3A%20%225a5da72e83e7280001435057%22%2C%22created_at%22%3A%20%222018-01-16T07%3A18%3A06.430Z%22%2C%22userLanguage%22%3A%20%22zh%22%2C%22env%22%3A%20%22production%22%2C%22version%22%3A%20%2211.21.3-private.8%22%2C%22daysSinceRegistered%22%3A%201141%2C%22timezone%22%3A%208%2C%22experiments%22%3A%20%5B%5D%2C%22%24os_version%22%3A%20%22Macintosh%3B%20Intel%20Mac%20OS%20X%2010_14_6%22%2C%22%24initial_referrer%22%3A%20%22http%3A%2F%2Fteambition.ximalaya.com%2Flogin%3F%22%2C%22%24initial_referring_domain%22%3A%20%22teambition.ximalaya.com%22%7D; mp_tbpanel__c=0', 'Content-Type': 'application/json;'}
        #     data.yaml = {'title': '接口测试专用_完成必修任务音频', 'subtitle': '接口测试专用_完成必修任务音频副标题', 'categoryId': 275, 'cover': 'http://imagev2.test.ximalaya.com/storages/68e9-audiotest/4D/57/CAoVdh8DkmkxAABAsQAAKXf3.jpeg!op_type=3&columns=400&rows=400', 'intro': '<div class="qxt-editor"><style>.qxt-editor p{color:#7f7f7f;line-height:1.5;font-size:15px;} </style><div></div><p class="xmapp_img_wrapper" style="display:block;position:relative;text-align: center"><img class="xmapp_img_preview" src="http://imagev2.test.ximalaya.com/storages/b020-audiotest/37/00/CAoVReEC_W1pAAA2xAAAFWkg.png!op_type=3&columns=391" title="" data.yaml-src="http://imagev2.test.ximalaya.com/storages/b020-audiotest/37/00/CAoVReEC_W1pAAA2xAAAFWkg.png!op_type=3&columns=391" data.yaml-origin="http://imagev2.test.ximalaya.com/storages/b020-audiotest/37/00/CAoVReEC_W1pAAA2xAAAFWkg.png!op_type=0" data.yaml-preview="http://imagev2.test.ximalaya.com/storages/b020-audiotest/37/00/CAoVReEC_W1pAAA2xAAAFWkg.png!op_type=3&columns=391" data.yaml-cut="http://imagev2.test.ximalaya.com/storages/b020-audiotest/37/00/CAoVReEC_W1pAAA2xAAAFWkg.png!op_type=3&columns=391" alt=""/></p><p class="xmapp_img_wrapper" style="display: block; position: relative;">阿瑟来得及分类及卡就是的房间拉萨节快乐的房间阿瑟看的房间开了家阿瑟的咖啡里看见啊就是打开肌肤拉萨进度快了房间收到反馈</p><p><span style="color: rgb(127, 127, 127); font-size: 15px;">阿瑟来得及分类及卡就是的房间拉萨节快乐的房间阿瑟看的房间开了家阿瑟的咖啡里看见啊就是打开肌肤拉萨进度快了房间收到反馈阿瑟来得及分类及卡就是的房间拉萨节快乐的房间阿瑟看的房间开了家</span><strong><span style="color: rgb(127, 127, 127); font-size: 15px;">阿瑟的咖啡里看见啊就是打开肌肤拉萨进度快了房间收到反馈阿瑟来得及分类及卡就是的房间拉萨节快乐的房间阿瑟看的房间开了家阿瑟的咖啡里看见啊就是打开肌肤拉萨进度快了房间收到反馈</span>惺惺惜惺惺</strong></p><p class="xmapp_img_wrapper" style="white-space: normal; position: relative;">阿瑟来得及分类及卡就是的房间拉萨节快乐的房间阿瑟看的房间开了家阿瑟的咖啡里看见啊就是打开肌肤拉萨进度快了房间收到反馈</p><p style="white-space: normal;">阿瑟来得及分类及卡就是的房间拉萨节快乐的房间阿瑟看的房间开了家阿瑟的咖啡里看见啊就是打开肌肤拉萨进度快了房间收到反馈阿瑟来得及分类及卡就是的房间拉萨节快乐的房间<span style="font-size: 18px; background-color: rgb(255, 0, 0);">阿瑟看的房间开了家阿瑟的咖啡里看见啊就是打开肌肤拉萨进度快了房间收到反馈阿瑟来得及分类及卡就是的房间拉萨节快乐的房间阿瑟看的房间开了家阿瑟的咖啡里看见啊就是打开肌肤拉萨进度快了房间收到反馈惺惺惜惺惺</span></p><p class="xmapp_img_wrapper" style="white-space: normal; position: relative;"><span style="font-size: 18px; background-color: rgb(255, 0, 0);">阿瑟来得及分类及卡就是的房间拉萨节快乐的房间阿瑟看的房间开了家阿瑟的咖啡里看见啊就是打开肌肤拉萨进度快了房间收到反馈</span></p><p style="white-space: normal;"><span style="background-color: rgb(255, 0, 0);"><span style="background-color: rgb(255, 0, 0); font-size: 18px;">阿瑟来得及分类及卡就是的房间拉萨节快乐</span>的房间阿</span>瑟看的房间开了家阿瑟的咖啡里看见啊就是打开肌肤拉萨进度快了房间收到反馈阿瑟来得及分类及卡就是的房间拉萨节快乐的房间阿瑟看的房间开了家阿瑟的咖啡里看见啊就是打开肌肤拉萨进度快了房间收到反馈阿瑟来得及分类及卡就是的房间拉萨节快乐的房间阿瑟看的房间开了家阿瑟的咖啡里看见啊就是打开肌肤拉萨进度快了房间收到反馈惺惺惜惺惺</p><p class="xmapp_img_wrapper" style="white-space: normal; position: relative;">阿瑟来得及分类及卡就是的房间拉萨节快乐的房间阿瑟看的房间开了家阿瑟的咖啡里看见啊就是打开肌肤拉萨进度快了房间收到反馈</p><p style="white-space: normal;">阿瑟来得及分类及卡就是的房间拉萨节快乐的房间阿瑟看的房间开了家阿瑟的咖啡里看见啊就是打开肌肤拉萨进度快了房间收到反馈阿瑟来得及分类及卡就是的房间拉萨节快乐的房间阿瑟看的房间开了家阿瑟的咖啡里看见啊就是打开肌肤拉萨进度快了房间收到反馈阿瑟来得及分类及卡就是的房间拉萨节快乐的房间阿瑟看的房间开了家阿瑟的咖啡里看见啊就是打开肌肤拉萨进度快了房间收到反馈惺惺惜惺惺</p><p class="xmapp_img_wrapper" style="white-space: normal; position: relative;">阿瑟来得及分类及卡就是的房间拉萨节快乐的房间阿瑟看的房间开了家阿瑟的咖啡里看见啊就是打开肌肤拉萨进度快了房间收到反馈</p><p style="white-space: normal;">阿瑟来得及分类及卡就是的房间拉萨节快乐的房间阿瑟看的房间开了家阿瑟的咖啡里看见啊就是打开肌肤拉萨进度快了房间收到反馈阿瑟来得及分类及卡就是的房间拉萨节快乐的房间阿瑟看的房间开了家阿瑟的咖啡里看见啊就是打开肌肤拉萨进度快了房间收到反馈阿瑟来得及分类及卡就是的房间拉萨节快乐的房间阿瑟看的房间开了家阿瑟的咖啡里看见啊就是打开肌肤拉萨进度快了房间收到反馈惺惺惜惺惺</p><p class="xmapp_img_wrapper" style="white-space: normal; position: relative;">阿瑟来得及分类及卡就是的房间拉萨节快乐的房间阿瑟看的房间开了家阿瑟的咖啡里看见啊就是打开肌肤拉萨进度快了房间收到反馈</p><p style="white-space: normal;">阿瑟来得及分类及卡就是的房间拉萨节快乐的房间阿瑟看的房间开了家阿瑟的咖啡里看见啊就是打开肌肤拉萨进度快了房间收到反馈阿瑟来得及分类及卡就是的房间拉萨节快乐的房间阿瑟看的房间开了家阿瑟的咖啡里看见啊就是打开肌肤拉萨进度快了房间收到反馈阿瑟来得及分类及卡就是的房间拉萨节快乐的房间阿瑟看的房间开了家阿瑟的咖啡里看见啊就是打开肌肤拉萨进度快了房间收到反馈惺惺惜惺惺</p><p><br/></p></div>', 'sharePic': 'http://imagev2.test.ximalaya.com/storages/bc29-audiotest/3A/62/CAoVReEC_W3iAAoPIAAAFWkm.png!op_type=0', 'cerCover': 'http://imagev2.test.ximalaya.com/storages/1723-audiotest/69/1B/CAoVQB8Di9QGABjz2wAAKWf8.png!op_type=3&columns=600&rows=900', 'assignType': 1, 'completeTaskCount': 1, 'stages': {'ret': 0, 'msg': '操作成功', 'data.yaml': [{'stageId': None, 'projectId': None, 'beginTime': '${beginTime}$', 'endTime': '${endTime}$', 'stageName': '接口测试专用_阶段一', 'checkinRule': 1, 'checkinLearnTime': 0, 'resources': [{'contentType': 6, 'resourceType': 6, 'type': 6, 'resourceId': 264525, 'id': 264525, 'courseId': 6387, 'courseTitle': '21课时音频课-未开启目录111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'title': '19', 'cover': 'http://imagev2.test.ximalaya.com/storages/663b-audiotest/65/02/CAoVOi0DVx2tAALAAwAAGARd.jpg!op_type=3&columns=90&rows=90', 'selected': False, 'bizType': 1}]}]}, 'enableCer': 1, 'enableUserProfit': 1, 'enableUserTask': 0, 'beginTime': '${beginTime}$', 'endTime': '${endTime}$', 'status': 1}
        #     cookie = None
        #     timeout = 10
        #     post()
