import logging
import re
from common.unit.initialize_relevance import ini_relevance
from common.unit.replace_relevance import single_replace as single_replace
from common.config_module.config_read import Config

root_path = '/Users/nali/AutoApiTest'
path = root_path + '/config/api_config.ini'


def conf_manage(org_param, name):

    """

    :param org_param: 配置文件中二级参数key例如：$URL_OMS$
    :param name: 配置文件中的一级参数
    :return: 配置文件中二级参数的value
    """
    try:

        cf = Config(path)
        param = cf.read_config(name)
        value = single_replace(org_param,param)
        return value

    except Exception as e:
        logging.exception("读取配置文件报错：%s" % e)
        raise


if __name__ == '__main__':
    org_param = conf_manage('${HEADERS_OMS}$', 'HEADERS')
    print(org_param)