def str_to_int(s):
    if s.isdigit() is True:
        return int(s)
    return s


if __name__ == '__main__':
    s = '43'
    print(str_to_int(s))