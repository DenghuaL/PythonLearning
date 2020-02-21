#!usr/bin/env python3
# -*- coding: utf-8 -*-


import socket, threading, time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1', 9999))

print('Bind UDP on 9999...')

def udplink(data, addr):
    print(threading.current_thread().name)
    print('Recive data from %s: %s' % addr)
    s.sendto(b'Hello, %s!' % data, addr)


while True:
    data, addr = s.recvfrom(1024)
    t = threading.Thread(target=udplink, args=(data, addr))
    t.start()
 
'''
while True:
    data, addr = s.recvfrom(1024)
    print('Recieve from %s: %s' % addr)
    s.sendto(b'Hello, %s' % data, addr)

'''