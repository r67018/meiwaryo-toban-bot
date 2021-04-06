import datetime
from group_config import *


def getLastDate():
    year = month = day = 0
    path = 'src/last_day_info/year.txt'
def getCriteriaDate():
    path = 'src/info/year.txt'
    with open(path, mode='r') as f:
        year = int(f.read())
    path = 'src/info/month.txt'
    with open(path, mode='r') as f:
        month = int(f.read())
    path = 'src/info/day.txt'
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
    path = 'src/info/group.txt'
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


def getNextDayMessage():
    group_index = (calGroup() + 1) % group_size
    next_day_group = main_group[group_index]
    next_dt = datetime.datetime.now() + datetime.timedelta(days=1)
    message = '{}/{}\n{}: {}'.format(
        next_dt.month,
        next_dt.day,
        next_day_group,
        name[next_day_group]
    )
    return message
