import datetime


main_group = ('A', 'B', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N')
room = {
    'A': '213B 214B',
    'B': '313B 314B',
    'C': '405B 406B',
    'E': '211B 311B 312B',
    'F': '403B 404B',
    'G': '206B 209B',
    'H': '310B 309B',
    'I': '401B 402B',
    'J': '204B 205B',
    'K': '305B 306B',
    'L': '201B 301B',
    'M': '202B 203B',
    'N': '303B 304B',
}
group_size = len(main_group)
group_per_day = 3
today_group = []
now_dt = datetime.datetime.now()


def setLastInfo(year, month, day, group):
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
        f.write(group)

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
    info = ''
    path = './last_day_info/reply.txt'
    with open(path, mode='r') as f:
        info = f.read()
    return info


def advanceGroup(group, index):
    global main_group, group_size
    index = (index + 1) % group_size
    group += main_group[index]
    return index


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
        for _ in range(group_per_day):
            last_group_index = advanceGroup(group=today_group, index=last_group_index)
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
