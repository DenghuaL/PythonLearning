#!usr/bin/env python3
# -*- coding: utf-8 -*-

'''
try:
    f = open('readme.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()
'''
'''
with open('readme.txt', 'r') as f:
    print(f.read())
'''
'''
with open('readme.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())

with open('test01.txt', 'a') as f:
    f.write("\nHello, World!")
'''

fpath = r'C:\Windows\system.ini'

with open(fpath, 'r') as f:
    s = f.read()
    print(type(s))
    print(s)


