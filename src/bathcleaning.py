import datetime
from group_config import *


def getCriteriaDate():
    path = 'src/last_day_info/year.txt'
    with open(path, mode='r') as f:
        year = int(f.read())
    path = 'src/last_day_info/month.txt'
    with open(path, mode='r') as f:
        month = int(f.read())
    path = 'src/last_day_info/day.txt'
    with open(path, mode='r') as f:
        day = int(f.read())
    return year, month, day


def calPassedDay():
    now_dt = datetime.datetime.now().date()
    year , month , day = getCriteriaDate()
    criteria_dt = datetime.date(year, month, day)
    dt_abs = abs(now_dt - criteria_dt)
    return dt_abs.days


def getCriteriaGroup():
    path = 'src/last_day_info/group.txt'
    with open(path, mode='r') as f:
        group = f.read()
    return group


def calGroup():
    now_dt = datetime.datetime.now()
    passed_day = calPassedDay()
    index = (main_group.index(getCriteriaGroup()) + passed_day) % group_size
    return index


def getTodayMessage():
    group_index = calGroup()
    today_group = main_group[group_index]
    now_dt = datetime.datetime.now()
    message = '{}/{}\n{}: {}'.format(
        now_dt.month,
        now_dt.day,
        today_group,
        name[today_group]
    )
    return message
