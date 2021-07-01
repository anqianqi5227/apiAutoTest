import json
import re
import common.unit.replace_relevance as replace
from common.unit.initialize_relevance import ini_relevance as ini_relevance
from common.config_module.config_read import Config


def read_json(case_name, file_name, path):
    """
    读取json文件
    :param case_name: case名称
    :param file_name: json文件名
    :param path: case路径
    :return: dict接口参数
    """
    # cf = Config(path)
    # cf.read_conf_value()
    with open(path + '/' + file_name, 'r') as file:

        json_file = json.load(file)
        # print(json_file)
        json_param = {}
        for i in range(len(json_file)):
            if json_file[i]['test_name'] == case_name:
                json_param = json_file[i]['parameter']
                break
            else:
                continue
        # print(json_param)
        return json_param


def tra_json(json, relevance):
    """
    递归dict数据结构并替换关联值
    :param json: dict数据
    :param relevance: 关联池
    :return: 替换关联池之后的dict
    """
    for key in json:
        # 判断是不是list
        if isinstance(json[key], list):
            for i, val in enumerate(json[key]):
                if isinstance(val, dict):
                    tra_json(val, relevance)
        else:
            value = replace.single_replace(json[key], relevance)
            json[key] = value

    return json


def read_param(case_name, case_param, case_path, relevance):
    """
    读取case中的接口parameter参数
    :param case_name: case名称
    :param case_param: case中的parameter值
    :param path: case路径
    :param relevance: 关联池
    :return: 替换关联池之后的接口参数
    """
    # 判断是否为dict
    if isinstance(case_param, dict):
        param = tra_json(case_param, relevance)
        return param
    elif isinstance(case_param, str):
        # 判断是否为参数文件
        if re.findall('(.*?)\.json', case_param):
            json = read_json(case_name, case_param, case_path)
            param = tra_json(json, relevance)
            return param
        else:
            case_param = replace.replace(case_param,relevance)
            return case_param
    else:
        return case_param

if __name__ == '__main__':
    root_path = '/Users/nali/AutoApiTest'
    path = root_path + "/TestCases/project"
    # rel = ini_relevance(root_path + "/TestCases/project/relevance.ini", 'relevance')
    # print(rel)
    # json_file = read_param('add_project', {'corpId':'${corpId}$','uid':'${uid}$'}, path, rel)
    json_file = read_param('add_project','${corpId}$', path)
    print(json_file)
