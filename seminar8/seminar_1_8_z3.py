# Задача 3
# Cписок, заполнен случайным образом нулями и единицами.
# Найти самую длинную непрерывную последовательность единиц и определить индексы первого и последнего элементов в ней.

import random

print("******** Task 3 ********")

list = []

for i in range(50):
    n = int(random.random() * 2)
    list.append(n)
    print(n, end='')
    if not ((i + 1) % 10): print()

count = 0
maxCount = 0
index = 0
i = 0

while i < len(list):
    if list[i] == 1:
        count += 1
    else:
        if count > maxCount:
            maxCount = count
            index = i - 1  # последовательность закончилась на предыдущем элементе
        count = 0
    i += 1

print("\nКоличество элементов: ", maxCount)
print("id первого элемента: ", index - maxCount + 1)
print("id последнего элемента: ", index)