import os
import allure
import logging
from Main import root_path
from common.config_module.config_read import Config
from common.unit.initialize_relevance import ini_relevance


def setupTest(relevance_path, case_data, relevance):
    """
    获取用例全部关联关系
    :param relevance_path: 全局（模块）关联池路径
    :param case_data: 测试文件字典
    :param relevance: 测试用例关联池
    :return: 用例最终关联池
    """
    relevance_dict = {}
    module_relevance_file = os.path.join(relevance_path, 'ModuleRelevance.ini')
    global_relevance_file = os.path.join(relevance_path, 'GlobalRelevance.ini')

    cf = Config(module_relevance_file)
    if 'case_id' in case_data is True and case_data['case_id'] == 1:
        # 清空模块关联池
        cf.add_conf('relevance')

    module_relevance = cf.read_config('relevance')
    # 读取全局关联池中的关联值写入本模块关联池
    cf_g = Config(global_relevance_file)
    global_relevance = cf_g.read_config('relevance')
    print('anqi')
    logging.info('xxx %s' % global_relevance)
    # 汇总三个关联池中关联字段
    for k in relevance:
        relevance_dict[k] = relevance[k]
    for k in module_relevance:
        relevance_dict[k] = module_relevance[k]
    for k in global_relevance:
        relevance_dict[k] = global_relevance[k]

    # print(relevance_dict)
    fin_relevance = ini_relevance(relevance_dict)
    logging.info('xx %s' % fin_relevance)

    return fin_relevance


if __name__ == '__main__':
    case_dict = {'case_id': 1}
    relevance = {
        'assignSign': '*gen_sign(curUidCode=_GAQsTvZuwo&projectId=${project_id}$&uids=${uid}$&secret=92b13c1b3b97492daa47a160cd6086ba)*',
        'beginTime': '*gen_stamp_date_today_begin_time()*', 'corpId': 43,
        'endTime': '*gen_stamp_date_today_end_time()*'}
    relevance_path = root_path + "/common/config_module/relevance"
    print(setupTest(relevance_path, case_dict, relevance))
