import logging
import re
import os
from common.unit.replace_function import replace_function
from common.config_module.config_read import Config
from common.unit.replace_relevance import replace


def read_relevance(path, key):
    """
    根据文件路径，读取文件并处理文件中包含的关联值和函数，返回关联值字典
    :param key: ini文件中的section
    :param path: 文件路径
    :return: 初始公共关联值
    """

    path = path + '/' + key + '.ini'
    print(path)
    if os.path.isfile(path) is True:

        cf = Config(path)
        rele_dict = cf.read_config(key)

        return rele_dict
    return {}

def ini_relevance(rele_dict):
    # 将关联池内自身关联参数替换
    for k in rele_dict:
        rele_dict[k] = replace(rele_dict[k], rele_dict)
    # print(rele_dict)
    # 查找函数并替换
    for k in rele_dict:
        if isinstance(rele_dict[k], str):
            func_name = re.findall("\*(.*?)\*", rele_dict[k])
            if func_name:
                for func_name_value in func_name:
                    # 查找函数参数
                    func_param = re.findall("\((.*?)\)", func_name_value)
                    if func_param:
                        for func_param_value in func_param:
                            func_value = replace_function(func_name_value, func_param_value)
                            rele_dict[k] = func_value
    return rele_dict


if __name__ == '__main__':
    root_path = '/Users/nali/AutoApiTest'
    relevance_path = root_path + "/tests/CommonApi/loginApi"
    path1 = root_path+'/tests/TestCases/project'
    profile_dict = read_relevance(relevance_path, 'relevance')
    print(profile_dict)
