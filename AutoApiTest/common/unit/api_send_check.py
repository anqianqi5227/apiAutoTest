import os
import allure
import logging
import common.unit.api_send as api_send
import common.unit.check_result as check_result
from common.unit.read_result_relevance import replace_result
from common.config_module.config_read import Config

root_path = '/Users/nali/AutoApiTest'
relevance_path = root_path + "/common/config_module/relevance"


def api_send_check(case_data, case_dict, case_path, relevance):
    """
    验证测试是否通过并且将接口参数中的关联字段写入关联池
    :param case_data: 测试case
    :param case_dict: 测试用例文件
    :param case_path: 用例文件路径
    :param relevance: 用例关联池

    """
    # 获取接口返回值
    # print(case_dict)
    # print(case_dict['is_run'])
    logging.info('h %s' % relevance)
    if case_data['is_run'] is not False:
            # or case_data['is_run'] is None:
        res = api_send.api_send(case_data, case_dict, case_path, relevance)
        print(res)
        test_name = case_data['test_name']
        check_data = case_data['check']
        code = res[0]
        data = res[1]
        # 验证接口
        check_result.check_result(test_name, check_data, code, data, case_path, relevance)
        # 获取case中关联键和其在接口response中的值

        relevance = replace_result(case_data, res[1])

        with allure.step("关联值写入关联池文件"):
            allure.attach(str(relevance),"接口中获取的关联值")
            # 将关联键值对存入关联池中
            if case_data['global_relevance'] is True:

                if relevance is not None:
                    cf = Config(os.path.join(relevance_path, 'GlobalRelevance.ini'))
                    for k in relevance:
                        cf.add_section_option('relevance', k, relevance[k])
            else:
                if relevance is not None:
                    cf = Config(os.path.join(relevance_path, 'ModuleRelevance.ini'))
                    for k in relevance:
                        cf.add_section_option('relevance', k, relevance[k])
    else:
        pass



if __name__ == '__main__':
    root_path = '/Users/nali/AutoApiTest'
    relevance_path = root_path + "/core/test.ini"
    res = (200, {'ret': 0, 'msg': '操作成功', 'data.yaml': 10177})
    case_dict = {'address': '/admin/api/project/target/assign', 'check_type': 'only_check_status',
                 'relevance': 'data.yaml'}

    # relevance = {'assignSign': 'C8D05D0ACB0F20305A64814BF94307D5', 'beginTime': 1615910400000, 'corpId': '43', 'endTime': 1615996799000}
    relevance_fin = replace_result(case_dict, res[1])
    print(relevance_fin)
    cf = Config(relevance_path)
    for k in relevance_fin:
        cf.add_section_option('relevance', k, relevance_fin[k])
