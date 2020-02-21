#!usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import namedtuple, deque, defaultdict, OrderedDict, ChainMap, Counter
import os, argparse

Point = namedtuple('Point', ['X', 'Y'])
Poi = namedtuple('Point', ['X', 'Y'])
p = Point(1, 2)
q = Poi(1, 2)
print(Point, Poi, Point==Poi, p == q)

dd = defaultdict(lambda  : 'N/A')

dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

c = Counter()
c.update('Hello, World!')
print(c)

defaults = {
    'color': 'red',
    'user': 'guest'
}

parser = argparse.ArgumentParser()
parser.add_argument('-u','--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}

combine = ChainMap(command_line_args, os.environ, defaults)

print('color = %s' % combine['color'])
print('user = %s' % combine['user'])