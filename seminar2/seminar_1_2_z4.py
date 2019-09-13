#task 4
# Написать программу, так обменивающий значения трех переменных x, y, z, чтобы выполнилось требование: x < y < z.

x = 10
y = 7
z = 3

a1 = a2 = a3 = 0 # временные переменные

a1 = z if (y > z and x > z) else y if (x > y) else x
a2 = y # a2 - самостоятельно :)
a3 = z if (y < z and x < z) else y if (y > x) else x
print ("%d < %d < %d" % (a1, a2, a3))