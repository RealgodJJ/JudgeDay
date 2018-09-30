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

    month_day_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                      7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    days = 0

    for value in range(1, month):
        days += month_day_dict[value]

    if is_leap_year(year) and month > 2:
        days += 1

    days += day

    print("这是{}年的第{}天".format(year, days))


if __name__ == '__main__':
    main()
