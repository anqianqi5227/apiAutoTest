# 获取本周第一天，本周最后一天
import datetime


def getWeekDate():

    date = datetime.date.today()

    begindate = date.replace(date.year, date.month, (date.day - date.isoweekday() + 1))
    enddate = date.replace(date.year, date.month, (date.day - date.isoweekday() + 7))
    beginDate = str(begindate.year) + str(begindate.month) + str(begindate.day)
    endDate = str(enddate.year) + str(enddate.month) + str(enddate.day)

    return beginDate, endDate


if __name__ == '__main__':
    s = getWeekDate()[0]

    print (s)