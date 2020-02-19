#!usr/bin/env python3
# -*- coding: utf-8 -*-

import time, threading, multiprocessing

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(0)
    print('thread %s ended.' % threading.current_thread().name)

print('thred %s is running...' % threading.current_thread().name)
t = threading.Thread(target= loop) # , name='Loopthread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)


#Lock

balance = 0
lock = threading.Lock()

def chang_it(n):
    global balance
    balance = balance + n
    balance = balance - n 


def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            chang_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t3 = threading.Thread(target=run_thread, args=(10,))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print(balance)

print(multiprocessing.cpu_count())


local_school = threading.local()

def process_thread(name):
    local_school.student = name
    process_student()

def process_student():
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

t1 = threading.Thread(target=process_thread, args=('Andy',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()





