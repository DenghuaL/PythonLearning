#!usr/bin/env python3
# -*- coding: utf-8 -*-

L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2

print(L[0:3])


L = list(range(100))
print(L[-10::5])

T = tuple(L)
print(T[:3])

def trim(s):
    if s == '':
        return s
    else:
        i = 0
        while i <= len(s)-1:
            if s[i] == ' ':
                i = i + 1
            else:
                break
        s = s[i-1:]

        if s[-1] != ' ':
            return s
        else: 
            j = -1
            while j >= -len(s):
                if s[j] != ' ':
                    break
                j = j - 1
            s = s[:j+1]  
            return s

tr = trim('                  ')
print(tr, len(tr))


            


