import pytest
import allure
from common.unit.initialize_yaml import ini_yaml
from common.unit.initialize_relevance import read_relevance
from common.unit.api_send_check import api_send_check
from common.unit.setupTest import setupTest
from Main import root_path, case_level, product_version
case_path = root_path + "/tests/TestCases/templateApi"
relevance_path = root_path + "/common/config_module/relevance"
case_dict = ini_yaml(case_path, "template")


@allure.feature(case_dict['test_info']['title'])
class Template:
    @pytest.fixture(scope='class')
    def setupClass(self):
        # 获取用例初始关联值
        self.rel = read_relevance(path=case_path, key='relevance')
        return self.rel

    @pytest.mark.skipif(case_dict["test_info"]["product_version"] in product_version,
                        reason="该用例所属版本为：{0}，在本次排除版本{1}内".format(case_dict["test_info"]["product_version"],
                                                                 product_version))
    @pytest.mark.skipif(case_dict["test_info"]["case_level"] not in case_level,
                        reason="该用例的用例等级为：{0}，不在本次运行级别{1}内".format(case_dict["test_info"]["case_level"], case_level))
    # @pytest.mark.run(order=case_dict["test_info"]["run_order"])
    @allure.severity(case_dict["test_info"]["case_level"])
    @pytest.mark.parametrize("case_data", case_dict["premise"], ids=[])
    def test_premise(self, case_data, setupClass):
        if case_data is not None:
            self.relevance = setupTest(relevance_path, case_data, setupClass)
            api_send_check(case_data, case_dict, case_path, self.relevance)
        else:
            pass

    @pytest.mark.skipif(case_dict["test_info"]["product_version"] in product_version,
                        reason="该用例所属版本为：{0}，在本次排除版本{1}内".format(case_dict["test_info"]["product_version"],
                                                                 product_version))
    @pytest.mark.skipif(case_dict["test_info"]["case_level"] not in case_level,
                        reason="该用例的用例等级为：{0}，不在本次运行级别{1}内".format(case_dict["test_info"]["case_level"], case_level))
    # @pytest.mark.run(order=case_dict["test_info"]["run_order"])
    @allure.severity(case_dict["test_info"]["case_level"])
    @pytest.mark.parametrize("case_data", case_dict["test_case"], ids=[])
    @allure.story("template")
    def test_case(self, case_data, setupClass):
        self.relevance = setupTest(relevance_path, case_data, setupClass)
        api_send_check(case_data, case_dict, case_path, self.relevance)


if __name__ == '__main__':
    import subprocess

    subprocess.call(['pytest', '-v'])