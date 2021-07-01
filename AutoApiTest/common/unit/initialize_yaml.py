import yaml


def ini_yaml(path, name):
    with open(path + '/' + name +'.yaml', "r") as file:
        file_new = file.read()
        file_dict = yaml.load(file_new)

    return file_dict


# def ini_yaml(path,name):
#     file_dict = read_yaml(path)
#     return file_dict[name]


if __name__ == '__main__':
    root_path = '/Users/nali/AutoApiTest'
    print(root_path)
    path = root_path + "/TestCases/project"

    data_dict = ini_yaml(path, 'data.yaml')
    print(data_dict)
# print(data_dict['test_info']['title'])
