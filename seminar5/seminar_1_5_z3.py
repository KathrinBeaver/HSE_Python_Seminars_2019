def recursiveFunc(m, n):
   if m == 0: # базовый случай
       return n + 1
   elif n == 0 and m > 0:
       return recursiveFunc(m - 1, 1)
   else:
       return recursiveFunc(m - 1, recursiveFunc(m, n - 1))

m = int(input("Введите m: "))
n = int(input("Введите n: "))
print("Значение функции А(%d, %d)=%d" % (m, n, recursiveFunc(m, n)))
