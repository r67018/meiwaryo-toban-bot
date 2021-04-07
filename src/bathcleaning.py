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
    return datetime.date(year, month, day)


def getCriteriaGroup():
    path = 'src/info/group.txt'
    with open(path, mode='r') as f:
        group = f.read()
    return group


def isAfterday(date):
    if date < getCriteriaDate():
        return False
    return True


def calPassedDay(dt):
    criteria_dt = getCriteriaDate()
    dt_abs = abs(dt - criteria_dt)
    return dt_abs.days


def calGroup():
    now_dt = datetime.datetime.now().date()
    passed_day = calPassedDay(now_dt)
    index = (main_group.index(getCriteriaGroup()) + passed_day) % group_size
    return index


def conversionMMDD(MMDD):
    month = int(MMDD[0] + MMDD[1])
    day = int(MMDD[2] + MMDD[3])
    return datetime.date(getCriteriaDate().year, month, day)


def getNdaysLetterMessage(n):
    group_index = (calGroup() + n) % group_size
    group = main_group[group_index]
    date = datetime.datetime.now() + datetime.timedelta(days=n)
    message = '{}/{}\n{}: {}'.format(
        date.month,
        date.day,
        group,
        name[group]
    )
    return message
