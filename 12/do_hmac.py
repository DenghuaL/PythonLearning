#!usr/bin/env python3
# -*- coding: utf-8 -*-

import hmac

message = b'Hello, world!'
key = b'secret'

h = hmac.new(key, message, digestmod='MD5')
print(h.hexdigest())

h2 = hmac.new(key, b'Hello, ', digestmod='MD5')
h2.update(b'world!')
print(h2.hexdigest())