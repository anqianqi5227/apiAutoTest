import configparser
import os


class ConfigOveride(configparser.RawConfigParser):
    # def __init__(self, defaults=None):
    #     ConfigParser.ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr


class Config(object):
    def __init__(self, path_file):

        self.path_file = path_file
        self.file = os.path.split(path_file)[1]
        self.path = os.path.split(path_file)[0]

    def add_conf(self, section):
        """
        向文件中写入section
        :param section: ini文件中section
        """
        cf = ConfigOveride()
        cf.add_section(section)

        with open(self.path_file, "w+") as f:
            cf.write(f)

    def add_section_option(self, section, option, value):
        """
        向文件中对应section下写入option,value的键值对
        :param section: ini文件中section
        :param option: ini文件中option
        :param value: ini文件中option的值
        """
        cf = ConfigOveride()
        os.chdir(self.path)
        cf.read(self.file)
        if value is None:
            value = ''

        if cf.has_section(section):
            # cf.clear()
            # if cf.has_option(section, option) is False:
            cf.set(section, option, value)

        else:
            # cf.clear()
            cf.add_section(section)
            cf.set(section, option, value)

        with open(self.path_file, "w+") as f:
            cf.write(f)

    def read_conf_value(self, option):
        """
        读取ini文件中的某个option的value值
        :param option: option
        :return: option对应的value
        """
        cf = ConfigOveride()
        os.chdir(self.path)
        cf.read(self.file)

        # 获取文件中全部section
        sec_list = cf.sections()
        for i in sec_list:
            # 获取该section下全部键值对，结果为list结构，每个键值对为元组结构
            key_value_list = cf.items(i)
            for k, val in enumerate(key_value_list):
                if val[0] == option:
                    return val[1]
        return None

    def read_config(self, section):
        """
        以dict方式返回ini文件中option键值对
        :param section: section
        :return: option键值对
        """
        cf = ConfigOveride()
        os.chdir(self.path)
        cf.read(self.file)

        option_value_dict = {}
        option_value_list = cf.items(section)
        for k, val in enumerate(option_value_list):
            option_value_dict[val[0]] = val[1]

        return option_value_dict


if __name__ == '__main__':
    relevance_path = '/Users/nali/AutoApiTest/common/config_module/relevance/relevance.ini'

    cf = Config(relevance_path)
    print(cf.read_config('relevance'))
