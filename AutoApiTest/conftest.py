import pytest
import allure
from Main import root_path
import logging
import os
from common.config_module.config_read import Config
import common.unit.initialize_relevance  as re
from common.unit.api_send_check import api_send_check
from common.unit.initialize_yaml import ini_yaml

conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config", "api_config.ini")

case_path = root_path + "/tests/CommonApi/loginApi"
relevance_path = root_path + "/common/config_module/relevance"
case_dict = ini_yaml(case_path, "login")


# @pytest.fixture(scope="session", autouse=True)
# def setup_env():
#     # 定义环境；定义报告中environment
#     Host = Config(conf_path).read_config("HOST")
#     allure.environment(测试环境="测试环境", hostName=Host["HOST2"], 执行人="安琪", 测试项目="m站线上接口测试")

@pytest.fixture(scope="session",autouse=True,params=case_dict['test_case'])
# @allure.step("登录m站")
def login(request):
    for i in ["GlobalRelevance.ini", "ModuleRelevance.ini"]:
        relevance_file = os.path.join(relevance_path, i)
        cf = Config(relevance_file)
        # print(relevance_file)
        cf.add_conf('relevance')
    logging.info("执行全局用例依赖接口，初始化数据！")
    relevance = re.ini_relevance(re.read_relevance(case_path, 'relevance'))
    # print(relevance)
    api_send_check(request.param, case_dict, case_path, relevance)
    logging.info("初始化数据完成！")

    yield
    logging.info("本轮测试已结束，正在还原测试环境！")

