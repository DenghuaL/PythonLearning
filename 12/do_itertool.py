#!usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools
from functools import reduce

def pi(N):
    'calculate pi'
    n = itertools.count(1)
    ns = itertools.takewhile(lambda x: x <= N, n)
    return reduce(lambda x, y: x + y, map(lambda x: (-1)**(x+1)*4/(2*x-1), ns) )


print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
