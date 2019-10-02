# Задача 2
# Требуется отсортировать список случайных чисел от 10 до 100 любым известным способом.

from random import random

myLst1 = []
# заполнение
for i in range(100):
    myLst1.append(10 + int(random() * 90))

# проверка
for j in myLst1: # для каждого элемента списка
    if (j < 10 or j > 100):
        print("Error in List: ", j)
        break
print("List was created")
# Сортировка
# ....
# ....
# ....
# вывод осортированного списка в виде таблицы 10*10
row = 0
for i in sorted(myLst1):
# for i in myLst1:
    print("%3d" % i, end = '')
    row += 1
    if not(row % 10):
        print()