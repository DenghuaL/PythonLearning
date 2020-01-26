#!/usr/bin/python3
# -*- coding:utf-8 -*-

l1 = [1,2,3,4]
l2 = [1,]
l3 = [2]                    #l3 is list
print(l1,l2,l3)

t1 = (1,2,3,4)
t2 = (1,)
t3 = (2)                    #t3 is a int not tuple

print(t1,t2,t3)

l1.append(5)                #.append(), .pop(), .insert()
print('l1 = %s\n' %l1)           


t = ('a','b',['A',"B"])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)