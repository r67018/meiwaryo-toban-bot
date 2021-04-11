import datetime as dt
from group_config import *


def getCriteriaDate():
    path = 'bot/info/year.txt'
    with open(path, mode='r') as f:
        year = int(f.read())
    path = 'bot/info/month.txt'
    with open(path, mode='r') as f:
        month = int(f.read())
    path = 'bot/info/day.txt'
    with open(path, mode='r') as f:
        day = int(f.read())
    return dt.date(year, month, day)


def getCriteriaGroup():
    path = 'bot/info/group.txt'
    with open(path, mode='r') as f:
        group = f.read()
    return group


def calPassedDay(date):
    criteria_dt = getCriteriaDate()
    dt_abs = abs(date - criteria_dt)
    return dt_abs.days


def calGroup(date):
    passed_day = calPassedDay(date)
    index = (main_group.index(getCriteriaGroup()) + passed_day * group_per_day) % group_size
    groups = []
    for _ in range(group_per_day):
        groups.append(main_group[index])
        index = (index + 1) % group_size
    return groups


def isAfterday(date):
    if date < getCriteriaDate():
        return False
    return True


def conversionMMDD(MMDD):
    month = int(MMDD[:2])
    day = int(MMDD[2:4])
    return dt.date(getCriteriaDate().year, month, day)


def getSpecificDateMessage(date):
    groups = calGroup(date)
    message = '{}/{}'.format(date.month, date.day)
    for group in groups:
        message += '\n{}: {}'.format(group, name[group])
    return message
