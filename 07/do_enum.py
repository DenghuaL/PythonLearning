#!usr/bin/env python3
#--*-- coding: utf-8 --*--

import enum
from enum import Enum, unique
from my_str import Fib

Month = Enum('Month', ('Jan','Feb', 'Mar','Apr','May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name,'==>', member, ',', member.value)

print(Month.__members__.items())

month1 = Month.Jan
print(month1)
print(Month.Feb)
print(Month['Mar'])
print(month1.value)
print(Month.Apr.value)
print(Month(5))
print(Month(Month.Jun))
print(type(Enum))

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(type(Weekday))


class Gender(Enum):
    Male = 0
    male = 0
    Female = 1
    female = 1

print(Gender.__members__.items())
print(Gender.Male, Gender.Male.name)
for gender in Gender:
    print(gender)


class Student(object):
    def __init__(self, name, gender):
        if gender in Gender:
            self.name = name
            self.gender = gender

bart = Student('Bart', Gender.male)
print(bart.gender)

print(enum.__file__)
print(type(bart))





