# coding=utf-8
"""
    author: RealgodJJ
    function: Judge the day of a year
    version: 1.0
    date: 2018/9/28
"""
from datetime import datetime


def is_leap_year(year):
    is_leap = False
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        is_leap = True
    return is_leap


def main():
    input_date_str = input('请输入日期(yyyy/mm/dd)：\n')
    input_date = datetime.strptime(input_date_str, '%Y/%m/%d')
    # print(input_date)

    year = input_date.year
    month = input_date.month
    day = input_date.day

    # 包含30天的月份集合
    _30_days_month_set = {4, 6, 9, 11}
    _31_days_month_set = {1, 3, 5, 7, 8, 10, 12}
    days = 0

    for value in range(1, month):
        if value in _30_days_month_set:
            days += 30
        elif value in _31_days_month_set:
            days += 31
        else:
            days += 28

    if is_leap_year(year) and month > 2:
        days += 1

    days += day

    print("这是{}年的第{}天".format(year, days))


if __name__ == '__main__':
    main()
