import allure
import pytest
from common.configModel import confRead
from Main import root_path
from common.unit.initializeYamlFile import ini_yaml
from common.unit.initializeRelevance import ini_relevance
from common.unit.apiSendCheck import api_send_check
from common.configModel.confRead import Config
import logging
import os

conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config", "apiConfig.ini")
case_path = root_path + "/tests/CommonApi/loginApi"
relevance_path = root_path + "/common/configModel/relevance"

@pytest.fixture(scope="session", autouse=True)
def setup_env():
    # 定义环境；定义报告中environment
    Host = confRead.Config(conf_path).read_apiConfig("host")
    allure.environment(测试环境="online", hostName=Host["host"], 执行人="XX", 测试项目="线上接口测试")


case_dict = ini_yaml(case_path, "login")

# 参数化 fixture
@pytest.fixture(scope="session", autouse=True, params=case_dict["test_case"])
def login(request):
    # setup
    """
    :param request: 上下文
    :param request.param: 测试用例
    :return:
    """
    # 清空关联配置
    for i in ["GlobalRelevance.ini", "ModuleRelevance.ini"]:
        relevance_file = os.path.join(relevance_path, i)
        cf = Config(relevance_file)
        cf.add_conf("relevance")

    logging.info("执行全局用例依赖接口，初始化数据！")
    relevance = ini_relevance(relevance_path, "ModuleRelevance")
    if request.param["case_id"] == 1:
        relevance = ini_relevance(case_path, "relevance")

    logging.info("本用例最终的关联数据为：{}".format(relevance))
    # 发送测试请求
    api_send_check(request.param, case_dict, case_path, relevance)
    logging.info("初始化数据完成！")
    yield
    # teardown
	# 还原测试环境部分代码
	……
	……
    logging.info("本轮测试已结束，正在还原测试环境！")