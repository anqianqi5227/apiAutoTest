import re, logging
from common.tools.format_change import str_to_int

def single_replace(org_param, relevance):
    """

    :param org_param: 需要替换的参数
    :param relevance: 关联池
    :return: 替换关联值
    """
    try:
        if isinstance(org_param, str):
            param = re.search('\${(.*?)}\$', org_param) \
                    or re.search('{(.*?)}', org_param)

            if param is not None:
                param = param.group(1)
                logging.info('param %s' % param)
                logging.info('relevance.keys() %s' % relevance.keys())
                if param in relevance.keys():

                    param_value = relevance[param]
                    logging.info('param_value %s' % param_value)
                    return param_value
                # else:
                #     return org_param
            elif param is None:
                return org_param
        else:
            return org_param

    except Exception as e:
        logging.error("匹配失败：%s" % e)


def replace(org_param, relevance):
    param_str = ''
    if isinstance(org_param,str):
        param_list = re.split('\$(.*?)\$', org_param)
        if param_list:
            for k, val in enumerate(param_list):
                val = single_replace(val, relevance)
                param_str += str(val)
            return str_to_int(param_str)
    return org_param

if __name__ == '__main__':
    org_param = "${name}$"
    relevance = {'beginTime': 1614614400000, 'endTime': 1614700799000, 'assignSign': 'F134BE3AE56D0B83236C4B0782E9269D',
                 'project_code': '43','name':'安琪'}
    value = replace(org_param, relevance)
    print(type(value))
    print(value)
