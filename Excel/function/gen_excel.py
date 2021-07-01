import xlwt
import phonenum.gen_phone_num as gen_phone_num
import random
import time

w = xlwt .Workbook("员工列表.xls")

ws = w.add_sheet("员工列表")


def getRandomValue(values):
    n = len(values)

    if n == 0:
        return None

    num = random.randint(0, n - 1)

    return values[num]


now = time.time()
for rows in range(0, 18000):

    phone = gen_phone_num.phone_num()

    for columns in range(0, 5):

        if columns == 0:
            ws.write(rows, columns, str(phone))
        elif columns == 1:
            ws.write(rows, columns, getRandomValue(['男', '女']))
        elif columns == 2:
            ws.write(rows, columns,str(phone))
        elif columns == 3:
            ws.write(rows, columns, phone)
        else:
            ws.write(rows, columns, getRandomValue(['4级', '3级', '5级','6级','7级','8级','9级','10级']))
print((time.time() - now))
w.save("员工列表.xls")
