import pytest
from common.unit.read_result_relevance import replace_result
from common.unit.initialize_yaml import ini_yaml
# from common.unit.initialize_premise import ini_request
from common.unit.api_send_check import api_send_check
from common.unit.initialize_relevance import read_relevance
from common.unit.api_send_check import api_send_check
from common.unit.setupTest import setupTest

root_path = '/Users/nali/AutoApiTest'
case_path = root_path + "/tests/TestCases/project"
relevance_path = root_path + "/common/config_module/relevance"
case_dict = ini_yaml(case_path, "data.yaml")


# print(case_dict["premise"][0]['parameter'])
# print(case_dict['parameter'])
class TestPremise:
    @pytest.fixture(scope='class')
    def setupClass(self):
        # 获取用例初始关联值
        self.rel = read_relevance(path=case_path, key='relevance')
        return self.rel

    @pytest.mark.parametrize("case_data", case_dict["premise"], ids=[])
    def test_premise(self, case_data, setupClass):
        # print(setupClass)
        self.relevance = setupTest(relevance_path, case_data, setupClass)
        api_send_check(case_data, case_dict, case_path, self.relevance)

    @pytest.mark.parametrize("case_data", case_dict["test_case"], ids=[])
    def test_case(self, case_data, setupClass):
        self.relevance = setupTest(relevance_path, case_data, setupClass)
        api_send_check(case_data, case_dict, case_path, self.relevance)


if __name__ == '__main__':
    pytest.main(["-q", "initialize_premise.py"])
