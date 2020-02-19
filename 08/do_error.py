#!usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' %s)
    return 10 / n

def bar(s):
    try :
        foo(s)
    except ValueError as e:
        print('ValueError!')
        raise ValueError('value %s' %s)
    

def main():
    try:
        bar(0)
    except Exception as e:
        logging.exception(e)

main()
print('END')


