import datetime
from group_config import *


def setLastInfo(year, month, day, group):
    global group_per_day

    #  set date
    path = './last_day_info/year.txt'
    with open(path, mode='w') as f:
        f.write(str(year))
    path = './last_day_info/month.txt'
    with open(path, mode='w') as f:
        f.write(str(month))
    path = './last_day_info/day.txt'
    with open(path, mode='w') as f:
        f.write(str(day))

    #  set last group
    path = './last_day_info/group.txt'
    with open(path, mode='w') as f:
        f.write(group[group_per_day - 1])

    #  set reply
    reply = '{}/{}\n{}: {}\n{}: {}\n{}: {}'.format(
        month, day,
        group[0], room[group[0]],
        group[1], room[group[1]],
        group[2], room[group[2]],
    )
    path = './last_day_info/reply.txt'
    with open(path, mode='w') as f:
        f.write(reply)


def getLastDate():
    year = month = day = 0
    path = './last_day_info/year.txt'
    with open(path, mode='r') as f:
        year = int(f.read())
    path = './last_day_info/month.txt'
    with open(path, mode='r') as f:
        month = int(f.read())
    path = './last_day_info/day.txt'
    with open(path, mode='r') as f:
        day = int(f.read())
    return year, month, day


def getLastGroup():
    path = './last_day_info/group.txt'
    with open(path, mode='r') as f:
        last_group = f.read()
    return last_group


def getReply():
    reply = ''
    path = './last_day_info/reply.txt'
    with open(path, mode='r') as f:
        reply = f.read()
    return reply


def advanceGroup(group, index):
    global main_group, group_size, group_per_day

    for _ in range(group_per_day):
        index = (index + 1) % group_size
        group += main_group[index]


def updateGroup():
    now_dt = datetime.datetime.now()
    last_year, last_month, last_day = getLastDate()
    last_dt = datetime.date(year=last_year, month=last_month, day=last_day)
    dt_abs = abs(now_dt.date() - last_dt)
    passed_day = dt_abs.days
    if passed_day == 0:
        return
    last_group_index = main_group.index(getLastGroup())

    today_group = None
    for _ in range(passed_day):
        today_group = []
        advanceGroup(group=today_group, index=last_group_index)
        # print(today_group)  # for debug

    setLastInfo(
        year=now_dt.year,
        month=now_dt.month,
        day=now_dt.day,
        group=today_group
    )


# def debug():
#     updateGroup()
#     print(getReply())


# debug()