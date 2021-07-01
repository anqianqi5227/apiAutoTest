import os
import re


def replace_file_name(case_dir):
    """
    根据用例目录生成脚本文件名并获取用例名称
    :param case_dir: 用例文件名
    :return: 脚本文件名，用例名称
    """
    # if isinstance(case_dir, str):
    case_dir = str(case_dir)
    # 根据路径获取case名称
    case_name = case_dir.split('.')[0]
    # 拼接脚本路径
    script_name = 'test_' + case_name + '.py'
    return script_name, case_name


def scan_cases(root_path, scan_path):
    """
    根据目录生成元组列表（脚本目录，用例名称）
    :param root_path: 根目录
    :param scan_path: 扫描目录
    :return: 脚本目录，用例名称
    """
    case_path_list = []
    test_case_path = root_path + scan_path
    # 遍历用例目录
    g = os.walk(test_case_path)
    for path, dir_list, file_list in g:
        for file_name in file_list:
            # 判断是否为yaml文件
            if '.yaml' in file_name:
                # 替换成脚本文件名 test_开头的py文件
                script_name = replace_file_name(file_name)
                file_path = path + '/' + script_name[0]
                case_path_tuple = (file_path, script_name[1])
                case_path_list.append(case_path_tuple)
    return case_path_list


def get_case_dir(root_path, scan_path):
    """
    根据目录生成元组列表（文件上级目录，脚本文件名，用例名称）
    :param root_path: 根目录
    :param scan_path: 扫描目录
    :return: 文件上级目录，脚本文件名，用例名称
    """
    case_dir_list = []
    # 根据目录生成元组列表（脚本目录，用例名称）
    case_path_list = scan_cases(root_path, scan_path)
    for i, case_path_tuple in enumerate(case_path_list):
        if isinstance(case_path_tuple[0], str):
            # 获取脚本文件名
            file = os.path.split(case_path_tuple[0])
            # 获取脚本文件上级目录
            case_dir = file[0].split('TestCases')[1]
            case_dir_tuple = (case_dir, file[1], case_path_tuple[1])
            case_dir_list.append(case_dir_tuple)
    return case_dir_list


def write_case_script(root_path, scan_path):
    """
    根据用例目录生成脚本目录，并根据模版生成脚本文件
    :param root_path: 根目录
    :param scan_path: 扫描路径
    """
    template_path = root_path + '/tests/TestScript/template.py'
    # 根据目录生成元组列表（文件上级目录，脚本文件名，用例名称）
    case_dir_list = get_case_dir(root_path, scan_path)
    # 打开模版文件，读出模版内容
    with open(template_path, 'r') as template_file:
        template_file = template_file.read()
        # 遍历元组列表
        for i, val in enumerate(case_dir_list):
            # 生成脚本目录
            script_dir = root_path + '/tests/TestScript' + val[0]
            # 判断目录是否存在，不存在则创建目录
            if not os.path.exists(script_dir):
                os.mkdir(script_dir)
            # 生成脚本最终绝对路径
            script_path = script_dir + '/' + val[1]
            # 根绝用例名称，替换模版内容，写入脚本文件
            case_name = val[2]
            # print(template_file)
            case_file1 = re.sub('template*', case_name, template_file)
            case_file = re.sub('Template*', 'Test' + str(case_name).capitalize(), case_file1)
            with open(script_path, 'w') as script_file:
                script_file.write(case_file)


if __name__ == '__main__':
    scan_path = '/tests/TestCases'
    root_path = '/Users/nali/AutoApiTest'
    case_path_list = scan_cases(root_path, scan_path)
    print(case_path_list)
    case_dir_list = get_case_dir(root_path, scan_path)
    print(case_dir_list)
    write_case_script(root_path, scan_path)
