#!usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def fact(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num == 1:
        return product
    else:
        return fact_iter(num-1, num*product)

test = 5

print('fact(%d) = ' %test, fact(test))


def move(n, a, b, c):
    if  n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
    return 0

move(3, 'A', 'B', 'C')
