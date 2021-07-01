

def read_relevance(case_dict):
    """
    读取测试用例中的关联值的key
    :param case_dict: 单条测试用例
    :return: 需加入关联池中的值的list
    """
    module_relevance = case_dict['relevance']
    # global_relevance = case_dict['global_relevance']
    # relevance = [module_relevance, global_relevance]
    case_relevance_dict = {}
    # 获取用例中的relevance值，存入list
    # if isinstance(module_relevance, dict):
    #     for k,val in module_relevance:
    #         case_relevance_dict[k] = .append(module_relevance[i])
    # # else:
    #     case_relevance_list.append(module_relevance)
    # return case_relevance_list


def replace_result(case_dict, result):
    """
    将接口response中的值取出存到字典中
    :param case_dict: 测试用例中的关联值的key的list
    :param result: 接口response
    :return: 当前接口的全部关联值dict
    """
    case_relevance_dict = case_dict['relevance']
    if isinstance(result, dict) and case_relevance_dict is not None:
        for i in case_relevance_dict:
            res = loop_data(case_relevance_dict[i], result)
            if res is not None:
                case_relevance_dict[i] = res
    return case_relevance_dict


def loop_data(key, result):
    """
    递归接口response的数据结构，获取key对应的value值
    :param key: 传入key
    :param result: 接口response
    :return: response中对应的value
    """
    if key in result:
        return result[key]
    for k in result:
        if isinstance(result[k], dict):
            return loop_data(key, result[k])

if __name__ == '__main__':
    res = (200, {'ret': 0, 'msg': '操作成功', 'data': 10142})
    case_dict = {'address': '/admin/api/project/target/assign', 'check_type': 'only_check_status','relevance':{'project_id' : 'data'}}
    # relevance = {'assignSign': 'C8D05D0ACB0F20305A64814BF94307D5', 'beginTime': 1615910400000, 'corpId': '43',
    #              'endTime': 1615996799000}
    relevance_fin = replace_result(case_dict, res[1])
    print(relevance_fin)


    # d = {
    #     'a': 1,
    #     'b': 2,
    #     'c': [{'aa': '2'}, {'aa': 3}],
    #     't': [1, 2, 3],
    #     'd': {
    #         'f': {
    #             'x': 12
    #         },
    #         'e': 55
    #     },
    #     'g': {
    #         'f': {
    #             'x': 12
    #         },
    #         'e': 55
    #     }
    # }
    # a = ['a','x','e']
    #
    # result = get_result_relevance_value(a,d)
