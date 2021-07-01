def check_json(src_data, dst_data):
    """
    校验的json
    :param src_data: 检验内容
    :param dst_data: 接口返回的数据
    :return:
    """
    if isinstance(src_data, dict):
        for key in src_data:
            if key not in dst_data:
                raise Exception("JSON格式校验，关键字%s不在返回结果%s中" % (key, dst_data))
            else:
                this_key = key
                if isinstance(src_data[this_key], dict) and isinstance(dst_data[this_key], dict):
                    check_json(src_data[this_key], dst_data[this_key])
                elif isinstance(type(src_data[this_key]), type(dst_data[this_key])):
                    raise Exception("JSON格式校验，关键字 %s 与 %s 类型不符" % (src_data[this_key], dst_data[this_key]))
                else:
                    pass
    else:
        raise Exception("JSON校验内容非dict格式")


def check_result(test_name, case, code, data, _path, relevance=None):
    """
    校验测试结果
    :param test_name: 测试名称
    :param case: 测试用例
    :param code: HTTP状态
    :param data: 返回的接口json数据
    :param relevance: 关联值对象
    :param _path: case路径
    :return:
    """
    # 不校验结果
    if case["check_type"] == 'no_check':
        with allure.step("不校验结果"):
            pass

    # json格式校验
    elif case["check_type"] == 'json':
        expected_result = case["expected_result"]
        if isinstance(case["expected_result"], str):
            expected_result = readExpectedResult.read_json(test_name, expected_result, _path, relevance)
        with allure.step("JSON格式校验"):
            allure.attach("期望code", str(case["expected_code"]))
            allure.attach('期望data', str(expected_result))
            allure.attach("实际code", str(code))
            allure.attach('实际data', str(data))
        if int(code) == case["expected_code"]:
            if not data:
                data = "{}"
            check_json(expected_result, data)
        else:
            raise Exception("http状态码错误！\n {0} != {1}".format(code, case["expected_code"]))

    # 只校验状态码
    elif case["check_type"] == 'only_check_status':
        with allure.step("校验HTTP状态"):
            allure.attach("期望code", str(case["expected_code"]))
            allure.attach("实际code", str(code))
            allure.attach('实际data', str(data))
        if int(code) == case["expected_code"]:
            pass
        else:
            raise Exception("http状态码错误！\n {0} != {1}".format(code, case["expected_code"]))

    # 完全校验
    elif case["check_type"] == 'entirely_check':
        expected_result = case["expected_result"]
        if isinstance(case["expected_result"], str):
            expected_result = readExpectedResult.read_json(test_name, expected_result, _path, relevance)
        with allure.step("完全校验结果"):
            allure.attach("期望code", str(case["expected_code"]))
            allure.attach('期望data', str(expected_result))
            allure.attach("实际code", str(code))
            allure.attach('实际data', str(data))
        if int(code) == case["expected_code"]:
            result = operator.eq(expected_result, data)
            if result:
                pass
            else:
                raise Exception("完全校验失败！ {0} ! = {1}".format(expected_result, data))
        else:
            raise Exception("http状态码错误！\n {0} != {1}".format(code, case["expected_code"]))

    # 正则校验
    elif case["check_type"] == 'Regular_check':
        if int(code) == case["expected_code"]:
            try:
                result = ""
                if isinstance(case["expected_result"], list):
                    with allure.step("正则校验"):
                        for i in case["expected_result"]:
                            result = re.findall(i.replace("\"","\'"), str(data))
                            allure.attach('正则校验结果\n',str(result))
                        allure.attach('实际data', str(data))
                else:
                    result = re.findall(case["expected_result"].replace("\"", "\'"), str(data))
                    with allure.step("正则校验"):
                        allure.attach("期望code", str(case["expected_code"]))
                        allure.attach('正则表达式', str(case["expected_result"]).replace("\'", "\""))
                        allure.attach("实际code", str(code))
                        allure.attach('实际data', str(data))
                        allure.attach(case["expected_result"].replace("\"", "\'") + '校验完成结果',
                                      str(result).replace("\'", "\""))
                if not result:
                    raise Exception("正则未校验到内容！ {}".format(case["expected_result"]))
            except KeyError:
                raise Exception("正则校验执行失败！ {}\n正则表达式为空时".format(case["expected_result"]))
        else:
            raise Exception("http状态码错误！\n {0} != {1}".format(code, case["expected_code"]))

    # 数据库校验
    elif case["check_type"] == "datebase_check":
        pass

    else:
        raise Exception("无该校验方式：{}".format(case["check_type"]))