#!usr/bin/env python3
#--*-- coding: utf-8 --*--

import functools, time

def log(*text):
    if text == ():
        text = '(you have no input at thi time)'
    def decorater(func):
        @functools.wraps(func)        
        def wrapper(*args, **kw):
            print('input = %s' % text)
            return func(*args, **kw)
        return wrapper    
    return decorater

@log()
def now():
    print('2020-2-14')


now()





def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        fn(*args, **kw)
        end = time.time()
        print('%s excuted in %.4f ms' % (fn.__name__, end - start))
        return fn(*args, **kw)
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y
@metric
def slow(x,y,z):
    time.sleep(0.1234)
    return x * y * z

print(fast(11,22))

print(slow(11,22,33))


def begin_end(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print('beginn call')
        return fn(*args, **kw)
    
    return wrapper

@begin_end
def test1():
    print('runing')

test1()




def log02(text):
    if isinstance(text, str):
        def decorater(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s begin call %s()' % (text, func.__name__))
                start = time.time()
                fr = func(*args, **kw)
                end = time.time()
                print('%s end call %s()' % (text, func.__name__))
                print('%s excuted in %.4f ms' % (func.__name__, end - start))
                return fr
            return wrapper
        return decorater
    else:
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print('begin call %s()' % (text.__name__))
            start = time.time()
            fr = text(*args, **kw)
            end = time.time()
            print('end call %s()' % (text.__name__))
            print('%s excuted in %.4f ms' % (text.__name__, end - start))
            return fr
        return wrapper

@log02
def test01():
    time.sleep(0.1234)
    print('running test01')

@log02('excute')
def test02():
    time.sleep(1.0000)
    print('running test02')

test01()

test02()
        