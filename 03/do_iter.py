#!usr/bin/env python3
# -*- coding: utf-8 -*-

def findMiandMax(L):
    if L == []:
        return(None, None)
    else :
        tempmax = L[0]
        for num in L:
            if num >= tempmax:
                tempmax = num
        tempmin = L[0]
        for num in L:
            if num <= tempmin:
                tempmin = num
        return (tempmin, tempmax)


print(findMiandMax([]))
print(findMiandMax([7]))
print(findMiandMax([7,1]))
print(findMiandMax([7,1,3,9,5]))