#!usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib, random

md5 = hashlib.md5()
#md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
md5.update('how to use md5 '.encode('utf-8'))
md5.update('in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

def calc_md5(password):
    #pass
    pw_md5 = hashlib.md5()
    pw_md5.update(password.encode('utf-8'))
    return pw_md5.hexdigest()

print(calc_md5('how to use md5 in python hashlib?'))

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9',
    
}

def login(user, password):
    if user in db:
        if db[user] == calc_md5(password):
            return True
        else:
            return False
    else:
        print('user(%s) not found!' % user)
        return False     

# 测试:
print('test01 starts ...')
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
assert not login('andy', '1234567890')
print('ok')


#the Salt MD5
def calc_salt_md5(password):
    return get_md5(password + 'the-Salt')


def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


'''
db = {}

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')
'''

def login(username, password):
    user = db[username]
    return user.password == get_md5(password + user.salt)



# 测试:
print('test02 starts ...')
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')