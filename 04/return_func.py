#!usr/bin/env python3
# -*- coding: utf-8 -*-


def createCounter():
    i = 0
    def counter():
        nonlocal i
        i = i + 1
        return i

    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA())


def is_odd(n):
    return n % 2 == 1

L1 = list(filter(is_odd, range(1, 20)))
print(L1)

L2 = list(filter(lambda x: x % 2 == 1,range(1, 20))) 
print(L2)

L3 = list(filter(lambda x: x % 2 != 1,range(1, 20))) 
print(L3)