#!usr/bin/env python3
# -*- coding: utf-8 -*-

import json
d = dict(name = 'Bob', age = 20, score = 89)
print('d = dict(): ',json.dumps(d))
print('d: ')

class Student(object):
    
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name' : std.name,
        'age' : std.age,
        'score' : std.score
    }

def dict2student(d):
    return Student(d['name'],d['age'], d['score']) 

s = Student('Bob', 20, 89)

print('default=student2dict: ',json.dumps(s, default=student2dict))

print('obj.__dict__: ',json.dumps(s,default=lambda obj: obj.__dict__))

json_str = json.dumps(s, default=student2dict)
print(json.loads(json_str, object_hook=dict2student))
print(s)

obj = dict(name = '小明', age = 20)
p = json.dumps(obj, ensure_ascii=True)
print(p) 