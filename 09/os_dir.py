#!usr/bin/env python3
# -*- coding: utf-8 -*-


import os
print(os.name)

#print(os.environ)

print(os.environ.get('PATH'))

srce_path = os.path.abspath('.')                #'.' means "current dir"

new = os.path.join(srce_path, 'testdir')

if 'testdir' in os.listdir('.'):
    os.rmdir(new)
os.mkdir(new)

print(os.path.abspath('.'))         #'.' means "current dir"

print(os.listdir())

print([x for x in os.listdir() if os.path.isdir(x)])

print([x for x in os.listdir() if os.path.isfile(x) and os.path.splitext(x)[1]=='.txt'])

print(os.listdir())