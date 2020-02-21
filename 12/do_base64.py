#!usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
def safe_base64_decose(s):
    if type(s) == bytes:
        s = str(s, encoding='utf-8')
    if len(s) % 4 == 0:
        return base64.b64decode(s)
    else:
        return base64.b64decode( s + '=' * (4 - (len(s) % 4)) )


print(safe_base64_decose(b'YWJjZA=='))
print(safe_base64_decose(b'YWJjZA'))

