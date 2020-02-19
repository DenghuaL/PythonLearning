#!usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    count = 0

    def __init__(self, name, gender, score):
        self.__name = name
        self.__gender = gender
        self.__score = score
        Student.count = Student.count + 1

        
        

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):

        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name    
    def get_gender(self):
        return self.__gender
    def get_score(self):
        return self.__score

    def set_gender(self,gender):
        if gender in ['M', 'F', 'm','f','male','female','Male','Female']:
            self.__gender = gender
        else:
            raise ValueError('bad gender input')


    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

print(Student.count)


lisa = Student('Lisa', 'female', 99)
print(Student.count)

bart = Student('Bart', 'Male', 75)
andy = Student('Andy', 'M', 58)
print(Student.count)

for std in [lisa, bart, andy]:
    print(std.get_name(), '  \t', std.get_gender(), '  \t', std.get_grade())

print('Student:', Student.count)

print(bart.count)