from requests_toolbelt import MultipartEncoder
import requests
import random
import os


def from_data(files):
    if files:
        for i in range(0, len(files)):
            # print(i)
            value = files[i]
            if '/' in value:
                file_parm = i
                print(files[file_parm])
                # files[file_parm] = (os.path.basename(value), open(value, 'rb'))
        return files



if __name__ == '__main__':
    # files = False
    files = ['/user']
    from_data(files)
