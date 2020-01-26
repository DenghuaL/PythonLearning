#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {'a': [1,2,3]}
key = (1,2,3)                       #dict中key的类型必须是不能变的
d[key] = 'a tuple'
print(d['a'])
print(d[key])
d[(3,4,5)] = 2020
print('\n')

print('(1,2,3)' in d)
print(key in d)
print('a' in d)
print('\n')

print(d.get('b'))
print('\n')

d['b'] = (4,5)
print(d)
print(d.pop('b'))
print(d)
print('\n******************分割线*******************\n\n')


s = set([1,2,3,4,5,2,3,4])
print(s)
s.add(6)
#s.add(6,7)
print(s)
s.remove(1)

s1 = set([1,2,3])
s2 = set([2,3,4])

print(s1 & s2)
print(s1 | s2)
print('\n')

a = ['c','b','a']
print(a.sort())
print(a)
b = 'abc'
print(b.replace('a','A'))                   # c = b.replace('a','A')    
                                            # print(c)
print(b)


