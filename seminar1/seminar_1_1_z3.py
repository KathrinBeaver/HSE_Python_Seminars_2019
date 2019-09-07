#Z3

from math import sqrt

a = int(input("Введите а: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
p = (a + b + c) / 2
s = sqrt(p * (p - a) * (p - b) * (p - c))
print ("Площадь равна: %g" % s)