import requests
import hashlib
#from core import gen_sign



def genSign(passport, password, passportType):

    str1 = 'passport=' + str(passport) + '&passportType=' + str(passportType) + '&password=' + str(password) + '&secret=f2b0c6a87c560f503b194ffef4c9226f'

    m = hashlib.md5()
    b = str1.encode(encoding='utf-8')
    m.update(b)

    sign = m.hexdigest()



    return sign.upper()


def login(passport, password, passportType, url):

    sign = genSign(passport, password, passportType)
    data = {'passport': passport,
            'password': password,
            'passportType': passportType,
            'sign': sign}
    res = requests.post(url, data)

    cookie = res.raw.headers.getlist('Set-Cookie')
    #n = len (cookie)


    str1 = cookie[0] + ';' + cookie[1] + ';' +  cookie[2] + ';' + cookie[3]



    return str1


if __name__ == '__main__':
    cookies = login(17521200974, 'anqi666', 1, 'https://www.test.qingxuetang.com/passport/api/pwdLogin')

    print('"cookies"' + ':' + '"' + cookies + '"')





