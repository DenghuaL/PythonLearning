#!usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from datetime import datetime, timedelta, timezone

#re.datetime = re.compile(r'(\d+)-(\d+)-(\d+)\s(\d+):(\d+):(\d+)')
re.timezone = re.compile(r'UTC([-|+]?\d+):00')


def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    #dt_match = re.datatime.match(dt_str)
    tz_match = re.timezone.match(tz_str)
    tz_info = timezone(timedelta(hours=int(tz_match.group(1))))
    dt = dt.replace(tzinfo=tz_info)

    return dt.timestamp()

print(to_timestamp('2015-6-1 08:10:30','UTC+7:00'))
print(to_timestamp('2015-5-31 16:10:30','UTC-09:00'))
    



'''
p = re.datetime.match('2015-6-1 08:10:30')
q = re.timezone.match('UTC-09:00')
print(p.groups(),q.groups())
'''
