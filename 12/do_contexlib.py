#!usr/bin/env python3
# -*- coding: utf-8 -*-



class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')
    
    def query(self):
        print('Query info about %s...' % self.name)


with Query('Bob') as q:
    q.query()


# @contextmanager 让我们通过编写generator来简化上下文管理

from contextlib import contextmanager

class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

#@contextmanager这个decorator接受一个generator，
#用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了
with create_query('Bob') as q: 
    q.query()

@contextmanager
def tag(name):
    print("<%s>" % name)            #1,with语句首先执行yield之前的语句，因此打印出<h1>；
    yield                           #2,yield调用会执行with语句内部的所有语句，因此打印出hello和world；
    print("</%s>" % name)           #3,最后执行yield之后的语句，打印出</h1>。

with tag("h1"):
    print("hello")
    print("world")



# @closing 它的作用就是把任意对象变为上下文对象，并支持with语句

from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.baidu.com')) as page:
    for line in page:
        print(line)

'''
closing是一个经过@contextmanager装饰的generator，编写起来很简单
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()

'''
    
   
