# import allure
# import pytest
# import time,os
# from Main import root_path, case_level, product_version, run_interval
from common.unit.initialize_yaml import ini_yaml
# from common.unit.initialize_premise import ini_request
from common.unit.api_send_check import api_send_check
from common.unit.initialize_relevance import ini_relevance
# from common.unit import setupTest
root_path = '/Users/nali/AutoApiTest'
case_path = root_path + "/TestCases/project"
relevance_path = root_path + "/TestCases/project/relevance.ini"
case_dict = ini_yaml(case_path, "test.yaml")
# case_path = root_path + "/TestCases/project"

# def test_project(case_data,case_dict,case_path):
    # """
    # 测试接口为：project
    # :param case_data: 测试用例
    # :return:
    # """
    # self.relevance = setupTest.setupTest(relevance_path, case_data, setupClass)
    # 发送测试请求
    # time.sleep(3)

case_data = case_dict['test_case'][0]
rel = ini_relevance(relevance_path, 'relevance')
r = api_send_check(case_data, case_dict, case_path, rel)

if r == 'hh':
   print('hh')
else:
    print('xxh')
    # import subprocess
    # subprocess.call(['pytest', '-v'])

