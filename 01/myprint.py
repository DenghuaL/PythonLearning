#!/usr/bin/env python3
#  -*- coding utf-8 -*-

print('hello,  %s\n'  %'world')
print('%2d - %03d = %02d\n' %(3,2,1))             # %03d, 保留3位输出，不足0补上
print('%.2f\n' % 3.1415926)                       # %,2f, 保留小数点后两位
print('Hello,{0},成绩提升了{1:.1f}%'.format('小明', 17.125))

s1 = 72
s2 = 85
r = (s2/s1 - 1) *100
print('成绩提升了 %.1d%%' %r)