import sys, os
import re
from contextlib import ExitStack
profileList = {}
def PropValue(inifile):
    with open(inifile) as profile:
        new_profile = profile.readlines()
        print(new_profile)
        for line in new_profile:
            line_key = line.strip().split("=", 1)[0]
            profileList[line_key] = line.strip().split("=", 1)[1]

def EnvReplaceYaml(yamlfile, newyamlfile):
    try:
        with ExitStack()  as stack:
            yml_file = stack.enter_context(open(yamlfile,'r+'))
            yml_output = stack.enter_context(open(newyamlfile,'w'))
            yml_file_lines = yml_file.readlines()
            for line in yml_file_lines:
                new_line = line
                if (new_line.find('$$PLACEHOLDER$$') > 0):
                    env_list = new_line.split(':')
                    env_name = env_list[0].strip()
                    replacement = ""
                    if env_name in profileList.keys():
                        replacement = profileList[env_name]
                    new_line = new_line.replace('$$PLACEHOLDER$$', replacement)
                yml_output.write(new_line)
    except IOError as e:
        print("Error: " + format(str(e)))
        raise


def yaml_variable_replace(yamlfile, newyamlfile):
    with ExitStack as stack:
        yaml_file = stack.enter_context(open(yamlfile, 'r+'))
        yaml_file_readline = yaml_file.readlines()
        for line in yaml_file_readline:
            kew_list = re.findall("\${2}(.*)\${2}", line)
            print(kew_list)
            if len(kew_list):
                for i in range(len(kew_list)):
                    key = kew_list[i].strip()
                    if key in profileList:
                        new_line = line.

            else:
                pass






if __name__ == "__main__":
    PropValue('env')
    EnvReplaceYaml('temp.yaml', 'newtemap.yaml')