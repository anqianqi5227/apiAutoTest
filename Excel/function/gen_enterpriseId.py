
import random
import xlrd
import xlwt


w = xlwt.Workbook("企业列表.xls")
ws = w.add_sheet("企业列表")

def getRandomValue(values):
    n = len(values)

    if n == 0:
        return None

    num = random.randint(0, n - 1)

    return values[num]

def getCellValues(row, column):

    w1 = xlrd.open_workbook("企业列表.xls")
    ws1 = w1.sheet_by_name("企业列表")

    values = ws1.cell(row, column).value

    return values


for rows in range(2, 100):

    enterpriseId = random.randint(0, 3000)

    for columns in range(0, 5):

        if columns == 0:
            ws.write(rows, columns, enterpriseId)
        elif columns == 1:
            ws.write(rows, columns, str(enterpriseId))
        elif columns == 2:
            ws.write(rows, columns, getRandomValue(['是', '否']))

        elif columns == 3:

            if str(getCellValues(rows, columns-1)) == str('是'):
                ws.write(rows, columns, 100)
            else:
                ws.write(rows, columns)

        elif columns == 4:
            ws.write(rows, columns, str("备注"))


w.save("企业列表.xls")