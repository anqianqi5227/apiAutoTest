import allure
import pytest
import time
# from Main import root_path, case_level, product_version, run_interval
from common.unit.initialize_yaml import ini_yaml
# from common.unit.initialize_premise import ini_request
from common.unit.api_send_check import api_send_check
from common.unit.initialize_relevance import ini_relevance
# from common.unit import setupTest

root_path = '/Users/nali/AutoApiTest'
case_path = root_path + "tests/TestCases/project"
relevance_path = root_path + "/common/config_model/relevance"
case_dict = ini_yaml(case_path, "parkinside")


# @allure.feature(case_dict["test_info"]["title"])
class TestProject:

    @pytest.fixture(scope="class")
    def setupClass(self):
        """
        :rel: 获取关联文件得到的字典
        :return:
        """
        self.rel = ini_relevance(case_path, 'relevance')     #获取本用例初始公共关联值
        self.relevance = ini_request(case_dict, case_path, self.rel)   #执行完前置条件后，得到的本用例最新全部关联值
        return self.relevance, self.rel


    # @pytest.mark.skipif(case_dict["test_info"]["product_version"] in product_version,
    #                     reason="该用例所属版本为：{0}，在本次排除版本{1}内".format(case_dict["test_info"]["product_version"], product_version))
    # @pytest.mark.skipif(case_dict["test_info"]["case_level"] not in case_level,
    #                     reason="该用例的用例等级为：{0}，不在本次运行级别{1}内".format(case_dict["test_info"]["case_level"], case_level))
    # @pytest.mark.run(order=case_dict["test_info"]["run_order"])
    @pytest.mark.parametrize("case_data", case_dict["test_case"], ids=[])
    # @allure.severity(case_dict["test_info"]["case_level"])
    # @pytest.mark.parkinside
    # @allure.story("parkinside")
    # @allure.issue("http://www.bugjira.com")  # bug地址
    # @allure.testcase("http://www.testlink.com")  # 用例连接地址
    def test_project(self, case_data, setupClass):
        """
        测试接口为：parkinside
        :param case_data: 测试用例
        :return:
        """
        self.relevance = setupTest.setupTest(relevance_path, case_data, setupClass)

        # 发送测试请求
        api_send_check(case_data, case_dict, case_path, self.relevance)
        time.sleep(10)


if __name__ == '__main__':

    import subprocess
    subprocess.call(['pytest', '-v'])