# Необходимо определить индексы элементов списка, значение которых не меньше заданного минимума и не больше заданного максимума.
# Cписок заполняется случайными числами в диапазоне от 0 до 99 (включительно) и состоит из 100 элементов.

import random

arr = []
for i in range(100):
    x = int(random.random() * 100)  # 0 <= x <= 99
    arr.append(x)
    print("%3d" % x, end='') # выравнивание при выводе
    if (i + 1) % 10 == 0:    # каждый 10й элемент с новой строки
        print()

minimum = int(input('Min: '))
maximum = int(input('Max: '))

index = []
for i in arr:
    # if minimum <= i <= maximum:  # 2 альтернативы, рекомендуется вторая
    if (minimum <= i) and (i <= maximum):
        index.append(arr.index(i))
print("Всего в интервале: ", len(index))
print("Индексы: ", index)