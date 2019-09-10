#Z3

# from math import sqrt
import math

a = int(input("Введите а: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print ("Площадь равна: %g, периметр равен %d" % (s, 2 * p))
print(s)
