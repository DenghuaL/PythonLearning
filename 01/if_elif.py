#!/usr/bin/env python3
# -*- coding: utf-8 -*-

weight = float(input('please input your weight(kg):' ))
height = float(input('please input your height(m):'))

BMI = weight/(height**2)

if BMI > 32:
    print('you are very fat!')
elif BMI >= 28:
    print('you are fat!')
elif BMI >= 25:
    print('you are over weight.')
elif BMI >= 18.5:
    print('you are fit')
elif BMI >=0:
    print('you are too thin')
else:
    print('UNKNOWN ERROR!')

print('BMI = %.2f\n' %BMI)