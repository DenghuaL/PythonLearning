#!usr/bin/env python3
# -*- coding: utf-8 -*-

L1 = [x**2 for x in range(1,11) if x**2 % 2 != 0]
print(L1)

L2 = [m+n for m in 'AB' for n in 'XY']
print(L2)

import os
L3 = [d for d in os.listdir()]
print(L3)

L4 = ['Hello', 'World', 'IBM', 'LaTax','Apple',';;']
L5 = [s.lower() for s in L4]
print(L5)

L6 = ['Hello', 'World', 'IBM', 'LaTax','Apple', 18, ';;', None]
L7 = [s.lower() if isinstance(s,str) else s for s in L6]
L8 = [s.lower() for s in L6 if isinstance(s,str)]
print(L7)
print(L8)

