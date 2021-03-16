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
    bc.setLastInfo(
        year=now_dt.year,
        month=now_dt.month,
        day=now_dt.day,
        group=today_group
    )


def retreat():
    today_group = []
    last_group_index = bc.main_group.index(bc.getLastGroup()) - bc.group_per_day - 1 % bc.group_size
    for _ in range(bc.group_per_day):
        last_group_index = bc.advanceGroup(group=today_group, index=last_group_index)

    now_dt = datetime.now()
    bc.setLastInfo(
        year=now_dt.year,
        month=now_dt.month,
        day=now_dt.day,
        group=today_group
    )
