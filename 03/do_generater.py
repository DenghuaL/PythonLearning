#!usr/bin/env python3
#--*-- coding: utf-8 --*--

def triangles():
    n = 1
    L = [1]
    
    while n < 10:
        yield L
        L.append(0)
        #L = [L[i-1] + L[i] for i in range(len(L))]
        M = list(range(len(L)))
        for i in range(len(L)):
            M[i] = L[i] + L [i-1]
        L = M
        n = n+1 

    return 'done'        

for chr in triangles():
    print(chr)



