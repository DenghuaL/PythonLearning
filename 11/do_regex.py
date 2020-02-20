#!usr/bin/env python3
# -*- coding: utf-8 -*-


import re

re_email = re.compile(r'^(<(.*)>\s)?([\w\.]+\.)?([\w]+)@([\w]+)\.(com|org)$')

def is_valid_email(addr):   
    re_match = re_email.match(addr)
    if re_match:
        return True
    else:
        return False

assert is_valid_email('someone01@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@exmple.com')


# print(is_valid_email('mr-bob@exmple.com'))
p = re_email.match(          '<> bill.bilibili.gates@microsoft.com'         )
print(p.groups())
print(p.groups()[0:])


def name_of_email(addr):
    re_match = re_email.match(addr)
    if re_match:
        if re_match.group(2):
            return str(re_match.group(2))
        else:
            if re_match.group(3) == None:
                gropu3 = ''
            return  str(gropu3 + re_match.group(4))
    else:
        return 'EMPTY NAME'

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org')
assert name_of_email('<> tom@voyager.org') == 'tom'


