# Задача 4
# Подсчитать количество уникальных элементов списка, содержащего 20 случайным образом заданных значений от 10 до 15 с шагом 0.5.

import random

myLst = [0] * 20 # пустой список из 20
for i in range(len(myLst)):
    myLst[i] = (20 + round(random.random() * 11)) / 2
print(myLst)

countUnique = 0

for i in range(len(myLst)):
    if not myLst[i] in myLst[i + 1:]:
        countUnique += 1

print("Количество уникальных элементов:", countUnique)
print("Второй способ: ", len(set(myLst)))