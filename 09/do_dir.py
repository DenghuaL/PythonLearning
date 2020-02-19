#!usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time

class Dirmember(object):

    def __init__(self, name):
        self._name = name
        self._mdate = os.path.getmtime(name)
        if os.path.isdir(name):
            self._type = '<DIR>'
        else:
            self._type = ''
        if os.path.isfile(name):
           self._size = os.path.getsize(name)
        else:
            self._size = ''

    def  listprint(self):
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(self._mdate)),'\t',self._type,'\t',self._size,'\t',self._name)


for x in os.listdir():
    a = Dirmember(x)
    a.listprint()
