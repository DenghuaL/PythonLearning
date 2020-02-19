#!usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

DIGIT = {
    '0':0, 
    '1':1, 
    '2':2, 
    '3':3, 
    '4':4, 
    '5':5, 
    '6':6, 
    '7':7, 
    '8':8, 
    '9':9
}

def str2int(s):
    def fn(x,y):
        return 10*x + y
    def char2num(s):
        return DIGIT[s]
    return reduce(fn, map(char2num, s))

def normalize(name):
    def Upp(s):
        if 'a' <= s <= 'z':
            return chr(ord(s) - 32)
        else:
            return s

    def low(s):
        if 'A' <= s <= 'Z':
            return chr(ord(s) + 32)
        else:
            return s

    name = list(map(low, name))
    name[0] = Upp(name[0])
    name = ''.join(name)

    return name
    
print(normalize('LISA'))


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize,L1))
print(L2)


def prod(L):
    def fn(x,y):
        return x * y
    return reduce(fn,L)

L3 = [3,5,7,9]
print(prod(L3))

CHAR_TO_FLOAT = {
    '0':0,
    '1':1,
    '2':2, 
    '3':3, 
    '4':4, 
    '5':5, 
    '6':6, 
    '7':7, 
    '8':8, 
    '9':9,
    '.':-1
}
def str2float(string):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch],string)
    point = 0

    def to_float(a,b):
        nonlocal point
        if b == -1:
            point = 1
            return a
        if point == 0:
            return a*10 + b
        else:
            point = point * 10
            return a + b / point
    return reduce(to_float, nums)

print(str2float('123.456'))
