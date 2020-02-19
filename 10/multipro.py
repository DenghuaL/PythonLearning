#!usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from multiprocessing import Process
from multiprocessing import Pool
import time, random
import subprocess
from multiprocessing import Queue 


'''
#poxis系统可以用fork函数创建子进程
print('process(%s) start...' % os.getpid())

pid = os.fork()
if pid ==0:
    print('I am child process(%s) and my father is %s.' %(os.getpid(), os.getppid()))
else:
    print('I(%s) just creata a child process(%s)' % (os.getpid, pid))

'''


'''
#创建一个子进程
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    
if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    p.start()
    p.join()
    print('child process end.')
'''

'''
#多进程池批量创建子进程
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(6):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocess done...')
    p.close()
    p.join()
    print('All subprocess done.')

'''



'''
#调用外部子进程，实现命令行输入命令
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
'''


'''
#通过命令行启用外部子进程后，还需要执行后续输入
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
'''

#进程之间的数据通信
def write(q):
    print('Process to write: %s' %os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read: %s' %os.getpid())
    while True:
        value = q.get()
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
