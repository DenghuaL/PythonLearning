#!usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__

    def __call__(self):
        print('My name is %s' % self.name)


print(Student('andy'))
s = Student('andy')
print(s)
print(s())

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b 
        if self.a > 100000:
            raise StopIteration
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start 
            stop = n.stop 
            if start is None:
                start = 0
            if stop is None:   
                raise ValueError('your inputed slice: [%s:%s] must have a stop index' % (n.start, n.stop))
                print()
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L


for n in Fib():
    if n < 100:
        print(n)
    else:
        print('end')
        break
 
print(Fib()[5:6])


class Chain(object):

    def __init__(self, path=''):
        self._path = path
    
    def __getattr__(self, path):
        if path == 'users':
            return lambda name: Chain('/%s' % name)
        return Chain('%s/%s' % (self._path, path))

    

        


    def __str__(self):
        return self._path
    __repr__ = __str__

print(Chain().users('lei').status.timeline.list)