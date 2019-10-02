# В матрице (n*n) заменить последний элемент каждой строки на сумму предыдущих элементов той же строки.
# Матрица - список списков (массив массивов)

import random

# размеры матрицы
n = 4
matrix = []
for i in range(n):  # формируем исходную матрицу
    line = []
    for j in range(n):
        line.append(int(random.random() * 11) - 5)  # от -5 до 5
    matrix.append(line)

for line in matrix:  # вывод исходной матрицы
    for i in line:
        print('%4d' % i, end='')
    print()

print()

for line in matrix:  # изменение матрицы
    sum = 0
    i = 0
    while i < n - 1:
        sum += line[i]
        i += 1
    else:
        line[n - 1] = sum

for line in matrix:  # вывод измененной матрицы
    for i in line:
        print('%4d' % i, end='')
    print()
