#!usr/bin/env python3
# -*- coding: utf-8 -*-

def odd_iter():
    m = 1
    while True:
        m = m + 2
        yield m
    
def not_divisible(y):
    return lambda x: x % y > 0

def primes():
    yield 2
    it = odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible(n), it)
        

for n in primes():
    if n < 100:
        print(n)
    else:
        break




def is_palindrome(n):
    string = str(n)
    inv_list = []
    
    
    while n >= 1:
        mod = n % 10
        inv_list.append(str(mod))
        n = n // 10
    
    
    inv_str = ''.join(inv_list)

    return string == inv_str

print(list(filter(is_palindrome,range(1,200))))

    
    
