# Created by:
# Date: 01.09
# Task description: Распечатать числа, заданные в 4х переменных  в строку
# через пробел, затем в столбик отступом в одну табуляцию.

# -*- coding: utf-8 -*-

import os
from os import path as p

a = 0
b = 10
c, d = 20, 30

print(a, b, c, d, end = "\n\t")
print(d, c, b, a, sep = "\n\t", end = "\n")

print(int(10.3))
print(int('0x10', 16))

print(float('+1.23'))
print(float('   -12345\n'))
print(float('1e-003'))
print(float('+1E6'))
print(float('-Infinity'))

s = "Hello %s!" % "Bob"
print(s)
print("или так: Привет, %s" % "Bob")
print('*' * 80)