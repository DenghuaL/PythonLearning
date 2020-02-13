#!/usr/bin/env python3
# --*-- coding:utf-8 --*--

import math

def my_abs(x): 
    if not isinstance(x,(int, float)):
        raise TypeError('bad operand type') 
    if x >= 0:
        return x
    else:
        return (-x)

print(my_abs(-100))

def nop():
    pass




def move(x,y,step,angel=0):
    nx = x + step * math.cos(angel)
    ny = y + step * math.sin(angel)
    return nx, ny

print(move(0,0,1))

def quatratic(a,b,c):
    dt = b**2 - 4*a*c
    x1 = ((-b) + math.sqrt(dt))/(2*a)
    x2 = ((-b) - math.sqrt(dt))/(2*a)
    return x1, x2

print('quadratic(2,3,1) = ', quatratic(2,3,1))
print('quatratic(1,3,-4) = ', quatratic(1,3,-4))



