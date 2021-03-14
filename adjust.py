import os
from datetime import datetime
import bathcleaning as bc


rePASSWORD = '^' + os.environ['PASSWORD'] + r'\s'
reADVANCE = r'\sadv$'
reRETREAT = r'\sret$'


def advance():
    today_group = []
    last_group_index = bc.main_group.index(bc.getLastGroup()) - bc.group_per_day + 1 % bc.group_size
    for _ in range(bc.group_per_day):
        last_group_index = bc.advanceGroup(group=today_group, index=last_group_index)

    now_dt = datetime.now()
    bc.setLastInfo(month=now_dt.month, day=now_dt.day, last_group=today_group)
    bc.setLastGroup(today_group[bc.group_per_day - 1])
    bc.setLastDate(now_dt.year, now_dt.month, now_dt.day)


def retreat():
    today_group = []
    last_group_index = bc.main_group.index(bc.getLastGroup()) - bc.group_per_day - 1 % bc.group_size
    for _ in range(bc.group_per_day):
        last_group_index = bc.advanceGroup(group=today_group, index=last_group_index)

    now_dt = datetime.now()
    bc.setLastInfo(month=now_dt.month, day=now_dt.day, last_group=today_group)
    bc.setLastGroup(today_group[bc.group_per_day - 1])
    bc.setLastDate(now_dt.year, now_dt.month, now_dt.day)
