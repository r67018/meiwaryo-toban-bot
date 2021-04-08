import datetime as dt
from group_config import *


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
    return dt.date(year, month, day)


def getCriteriaGroup():
    path = 'src/info/group.txt'
    with open(path, mode='r') as f:
        group = f.read()
    return group


def calPassedDay(date):
    criteria_dt = getCriteriaDate()
    dt_abs = abs(date - criteria_dt)
    return dt_abs.days


def calGroup(date):
    passed_day = calPassedDay(date)
    index = (main_group.index(getCriteriaGroup()) + passed_day) % group_size
    return index


def isAfterday(date):
    if date < getCriteriaDate():
        return False
    return True


def conversionMMDD(MMDD):
    month = int(MMDD[:2])
    day = int(MMDD[2:4])
    return dt.date(getCriteriaDate().year, month, day)


def getSpecificDateMessage(date):
    group_index = calGroup(date)
    group = main_group[group_index]
    message = '{}/{}\n{}: {}'.format(
        date.month,
        date.day,
        group,
        name[group]
    )
    return message
