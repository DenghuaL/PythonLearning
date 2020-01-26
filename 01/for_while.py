#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)

print(list(range(5)))
print(list(range(1,5)))
sum = 0
for x in range(101):
    sum = sum + x
print(sum) 

n = 99
sum = 0
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

n = 0
while n < 10:
    n = n + 1
    if n % 2 ==0:
        continue
    print(n)
print('END\n')

n = 1
while n < 10:
    print(n)
    n = n + 2
    
print('END')
