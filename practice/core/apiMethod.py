from Main import root_path, case_level, product_version, run_interval
from common.unit.initializeYamlFile import ini_yaml
from common.unit.initializePremise import ini_request
from common.unit.apiSendCheck import api_send_check
from common.unit.initializeRelevance import ini_relevance
from common.unit import setupTest
import requests
import json
import random
import os
from requests_toolbelt import MultipartEncoder

def post(header, address, request_parameter_type, timeout=8, data=None, files=None, cookie=None):
    """
    post请求
    :param header: 请求头
    :param address: 请求地址
    :param request_parameter_type: 请求参数格式（form_data,raw）
    :param timeout: 超时时间
    :param data: 请求参数
    :param files: 文件路径
    :return:
    """
    if 'form_data' in request_parameter_type:
        for i in files:
            value = files[i]
            if '/' in value:
                file_parm = i
                files[file_parm] = (os.path.basename(value), open(value, 'rb'))
        enc = MultipartEncoder(
            fields=files,
            boundary='--------------' + str(random.randint(1e28, 1e29 - 1))
        )
        header['Content-Type'] = enc.content_type

        response = requests.post(url=address, data=enc, headers=header, timeout=timeout, cookies=cookie)

    elif 'data' in request_parameter_type:
        response = requests.post(url=address, data=data, headers=header, timeout=timeout, files=files, cookies=cookie)

    elif 'json' in request_parameter_type:
        response = requests.post(url=address, json=data, headers=header, timeout=timeout, files=files, cookies=cookie)

    try:
        if response.status_code != 200:
            return response.status_code, response.text
        else:
            return response.status_code, response.json()
    except json.decoder.JSONDecodeError:
        return response.status_code, ''
    except simplejson.errors.JSONDecodeError:
        return response.status_code, ''
    except Exception as e:
        logging.exception('ERROR')
        logging.error(e)
        raise


def get(header, address, data, timeout=8, cookie=None):
    """
    get请求
    :param header: 请求头
    :param address: 请求地址
    :param data: 请求参数
    :param timeout: 超时时间
    :return:
    """
    response = requests.get(url=address, params=data, headers=header, timeout=timeout, cookies=cookie)
    if response.status_code == 301:
        response = requests.get(url=response.headers["location"])
    try:
        return response.status_code, response.json()
    except json.decoder.JSONDecodeError:
        return response.status_code, ''
    except simplejson.errors.JSONDecodeError:
        return response.status_code, ''
    except Exception as e:
        logging.exception('ERROR')
        logging.error(e)
        raise


def put(header, address, request_parameter_type, timeout=8, data=None, files=None, cookie=None):
    """
    put请求
    :param header: 请求头
    :param address: 请求地址
    :param request_parameter_type: 请求参数格式（form_data,raw）
    :param timeout: 超时时间
    :param data: 请求参数
    :param files: 文件路径
    :return:
    """
    if request_parameter_type == 'raw':
        data = json.dumps(data)
    response = requests.put(url=address, data=data, headers=header, timeout=timeout, files=files, cookies=cookie)
    try:
        return response.status_code, response.json()
    except json.decoder.JSONDecodeError:
        return response.status_code, ''
    except simplejson.errors.JSONDecodeError:
        return response.status_code, ''
    except Exception as e:
        logging.exception('ERROR')
        logging.error(e)
        raise


def delete(header, address, data, timeout=8, cookie=None):
    """
    delete请求
    :param header: 请求头
    :param address: 请求地址
    :param data: 请求参数
    :param timeout: 超时时间
    :return:
    """
    response = requests.delete(url=address, params=data, headers=header, timeout=timeout, cookies=cookie)

    try:
        return response.status_code, response.json()
    except json.decoder.JSONDecodeError:
        return response.status_code, ''
    except simplejson.errors.JSONDecodeError:
        return response.status_code, ''
    except Exception as e:
        logging.exception('ERROR')
        logging.error(e)
        raise


def save_cookie(header, address, request_parameter_type, timeout=8, data=None, files=None, cookie=None):
    """
    保存cookie信息
    :param header: 请求头
    :param address: 请求地址
    :param timeout: 超时时间
    :param data: 请求参数
    :param files: 文件路径
    :return:
    """
    cookie_path = root_path + '/common/configModel/relevance/cookie.ini'
    if 'data' in request_parameter_type:
        response = requests.post(url=address, data=data, headers=header, timeout=timeout, files=files, cookies=cookie)

    elif 'json' in request_parameter_type:
        response = requests.post(url=address, json=data, headers=header, timeout=timeout, files=files, cookies=cookie)

    try:
        if response.status_code != 200:
            return response.status_code, response.text

        else:
            re_cookie = response.cookies.get_dict()
            cf = Config(cookie_path)
            cf.add_section_option('relevance', re_cookie)
            for i in re_cookie:
                values = re_cookie[i]
                logging.debug("cookies已保存，结果为：{}".format(i+"="+values))
            return response.status_code, response.json()

    except json.decoder.JSONDecodeError:
        return response.status_code, ''
    except simplejson.errors.JSONDecodeError:
        return response.status_code, ''
    except Exception as e:
        logging.exception('ERROR')
        logging.error(e)
        raise
    ……………………