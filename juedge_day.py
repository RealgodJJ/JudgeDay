# coding=utf-8
"""
    author: RealgodJJ
    function: Judge the day of a year
    version: 1.0
    date: 2018/9/28
"""
from _datetime import datetime


def main():
    input_date_str = input('请输入日期(yyyy/mm/dd)：\n')
    input_date = datetime.strptime(input_date_str, '%Y/%m/%d')
    print(input_date)

    year = input_date.year
    month = input_date.month
    day = input_date.day

    # 计算之前每月天数总和以及当前月份天数（假设为平年）
    days_in_month_tup = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    days = sum(days_in_month_tup[: month - 1]) + day

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        if month > 2:
            days += 1

    print("这是第{}天".format(days))


if __name__ == '__main__':
    main()
