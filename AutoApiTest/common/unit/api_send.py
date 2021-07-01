import common.unit.api_method as api_method
import logging
from common.unit.initialize_relevance import read_relevance
from common.unit.read_json import read_param
from common.unit.replace_relevance import replace
from common.config_module.config_manage import conf_manage
import json
import allure

root_path = '/Users/nali/AutoApiTest'


def api_send(case_dict, prarm_dict, path, relevance):
    try:
        cur_host = prarm_dict['test_info'].get('host')
        cur_address = prarm_dict['test_info'].get('address')
        cur_headers = prarm_dict['test_info'].get('headers')
        cur_http_type = prarm_dict['test_info'].get('http_type')
        cur_request_type = prarm_dict['test_info'].get('request_type')
        cur_parameter_type = prarm_dict['test_info'].get('parameter_type')
        cur_cookies = prarm_dict['test_info'].get('host')
        cur_file = prarm_dict['test_info'].get('file')
        cur_timeout = prarm_dict['test_info'].get('timeout')

    except Exception as e:
        logging.exception("获取用例基本信息失败 %s " % e)

    try:
        # 若case中填写host关键字的值，则使用case中的host值，若case中没有host关键字，则使用全局传入的默认值
        cur_host = case_dict['host']
    except KeyError:
        pass
    try:
        # 若case中填写address关键字的值，则使用case中的address值，若case中没有address关键字，则使用全局传入的默认值
        cur_address = case_dict['address']
    except KeyError:
        pass
    try:
        # 若case中填写headers关键字的值，则使用case中的headers值，若case中headers关键字值为空，则此处headers值处理为None，
        # 若case中没有headers关键字，则使用全局传入的默认值
        cur_headers = case_dict['headers']
    except KeyError:
        pass
    try:
        cur_http_type = case_dict['http_type']
    except KeyError:
        pass
    try:
        cur_parameter_type = case_dict['parameter_type']
    except KeyError:
        pass
    try:
        cur_request_type = case_dict['request_type']
    except KeyError:
        pass
    try:
        cur_cookies = case_dict['cookies']
    except KeyError:
        pass
    try:
        cur_file = case_dict['file']
    except KeyError:
        pass
    try:
        cur_timeout = case_dict['timeout']
    except KeyError:
        pass

    cookie = None
    if cur_cookies is True:
        cookie_path = root_path + "/common/config_module/relevance"
        cookie = read_relevance(cookie_path, 'cookie')
        logging.debug("cookie处理结果为：%s" % cookie)
    else:
        pass
    print(cookie)
    parameter = read_param(case_dict['test_name'], case_dict['parameter'], path, relevance)
    print(parameter)
    logging.debug("请求参数处理结果：%s" % parameter)

    address = replace(cur_address, relevance)
    print(address)
    logging.debug("请求地址处理结果：%s" % cur_address)

    host = conf_manage(cur_host, 'HOST')
    print(host)
    logging.debug("host地址处理结果：%s" % host)
    # print(cur_headers)
    if isinstance(cur_headers, str):
        # print(conf_manage(cur_headers, 'HEADERS'))
        headers = json.loads(conf_manage(cur_headers, 'HEADERS'))
        logging.debug("请求头处理结果为：{}".format(headers))
        print(headers)
        # print(headers)
    if cur_request_type == 'post':

        logging.info("请求方法为 %s" % 'post')
        with allure.step("POST请求接口"):
            allure.attach(case_dict["test_name"], "请求接口：")
            allure.attach(case_dict["info"], "用例描述：")
            allure.attach(cur_http_type + "://" + host + address, "请求地址")
            allure.attach(str(headers), "请求头")
            allure.attach(str(parameter), "请求参数")
        result = api_method.post(url=cur_http_type + '://' + host + address,
                                 request_parameter_type=cur_parameter_type,
                                 headers=headers,
                                 timeout=cur_timeout,
                                 data=parameter,
                                 cookie=cookie)
        logging.info("请求接口结果：\n {}".format(result))
        return result

    elif cur_request_type == 'get':
        logging.info("请求方法为 %s" % 'get')
        with allure.step("get请求接口"):
            allure.attach(case_dict["test_name"], "请求接口：")
            allure.attach(case_dict["info"], "用例描述：")
            allure.attach(cur_http_type + "://" + host + address, "请求地址")
            allure.attach(str(headers), "请求头")
            allure.attach(str(parameter), "请求参数")
        result = api_method.get(url=cur_http_type + '://' + host + address,
                                data=parameter,
                                headers=headers,
                                timeout=cur_timeout,
                                cookie=cookie)
        logging.info("请求接口结果：\n {}".format(result))
        return result
    elif cur_request_type == 'post_cookie':
        with allure.step("POST请求接口"):
            allure.attach(case_dict["test_name"], "请求接口：")
            allure.attach(case_dict["info"], "用例描述：")
            allure.attach(cur_http_type + "://" + host + address, "请求地址")
            allure.attach(str(headers), "请求头")
            allure.attach(str(parameter), "请求参数")
        result = api_method.save_cookie(url=cur_http_type + '://' + host + address,
                                        request_parameter_type=cur_parameter_type,
                                        headers=headers,
                                        timeout=cur_timeout,
                                        data=parameter,
                                        cookie=cookie)
        return result

    else:
        result = {"code": False, "data": False}
        logging.info("没有找到对应的请求方法！")
        logging.info("请求接口结果：\n {}".format(result))
        return result
