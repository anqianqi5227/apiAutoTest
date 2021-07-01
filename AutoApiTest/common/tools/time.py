#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
import time


def today_datetime():
    """

    :return: 返回当天日期，当天日期+时间
    """
    now_date = datetime.date.today()
    now_datetime = datetime.datetime.now()
    return now_date, now_datetime, now_date.strftime("%Y%m%d")


def gen_timestamps_13(str_date):
    """

    :param str_date: 时间字符串
    :return: 13位时间戳
    """
    time_strp = time.strptime(str_date, "%Y-%m-%d %H:%M:%S")
    time_stamp = int(time.mktime(time_strp)) * 1000

    return time_stamp


def gen_stamp_date_today_begin_time():
    """

    :return: 当天00：00：00时间戳
    """
    begin_time_stamp = int(time.mktime(today_datetime()[0].timetuple())) * 1000
    # end_time_stamp = int(time.mktime((today_datetime()[0] + datetime.timedelta(1)).timetuple())) * 1000 - 1000

    return begin_time_stamp


def gen_stamp_date_today_end_time():
    """

    :return: 当天23：59：59分时间戳
    """
    # begin_time_stamp = int(time.mktime(today_datetime()[0].timetuple())) * 1000
    end_time_stamp = int(time.mktime((today_datetime()[0] + datetime.timedelta(1)).timetuple())) * 1000 - 1000

    return end_time_stamp


def this_week_date_begin():
    """

    :return: 本周第一天日期，本周最后一天日期
    """
    today_date = today_datetime()[0]
    this_week_begin = today_date - datetime.timedelta(today_date.weekday())
    # this_week_end = today_date + datetime.timedelta(6 - today_date.weekday())
    # print(this_week_end.strftime("%Y%m%d"))
    return this_week_begin.strftime("%Y%m%d")


def this_week_date_end():
    """

    :return: 本周第一天日期，本周最后一天日期
    """
    today_date = today_datetime()[0]
    this_week_beginin = today_date - datetime.timedelta(today_date.weekday())
    this_week_end = today_date + datetime.timedelta(6 - today_date.weekday())
    # print(this_week_end.strftime("%Y%m%d"))
    return this_week_end.strftime("%Y%m%d")


def this_month_data_begin():
    """

    :return: 本月第一天日期，本月最后一天日期
    """
    today_date = today_datetime()[0]
    this_month_begin = datetime.datetime(today_date.year, today_date.month, 1)
    # year = today_date.year
    # month = today_date.month
    # if today_date.month + 1 > 12:
    #     year = today_date.year + 1
    #     month = 1
    # this_month_end = datetime.datetime(year, month, 1) - datetime.timedelta(1)
    return this_month_begin.strftime("%Y%m%d")


def this_month_data_end():
    """

    :return: 本月第一天日期，本月最后一天日期
    """
    today_date = today_datetime()[0]
    # this_month_begin = datetime.datetime(today_date.year, today_date.month, 1)
    year = today_date.year
    month = today_date.month
    if today_date.month + 1 > 12:
        year = today_date.year + 1
        month = 1
    this_month_end = datetime.datetime(year, month, 1) - datetime.timedelta(1)
    return this_month_end.strftime("%Y%m%d")


if __name__ == '__main__':
    print(today_datetime())
    # print(datetime.date.today() - datetime.timedelta(1))
    # print(this_week_date())
    # print(this_month_data())
