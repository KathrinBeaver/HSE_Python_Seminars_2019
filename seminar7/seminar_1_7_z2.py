# В списке, состоящем из 20 положительных и отрицательных целых чисел [-50; 50], найти первый, третий
# и шестой положительные элементы и вычислить их произведение.
# На заметку: третий по счету положительный элемент может быть далеко не третим в списке.

import random

arr = list()
for i in range(20):
    arr.append(int(random.random() * 101) - 50)
print(arr)

i = 0
j = 1
ind1 = ind3 = ind6 = 0
while i < 20:
    if arr[i] > 0:
        if j == 1:
            ind1 = i
        elif j == 3:
            ind3 = i
        elif j == 6:
            ind6 = i
            break
        j += 1
    i += 1
if ind6 > 0: # если всё нашлось
    mult = arr[ind1] * arr[ind3] * arr[ind6]
    print("Индексы элементов:", ind1, ind3, ind6)
    print("%d * %d * %d = %d" % (arr[ind1], arr[ind3], arr[ind6], mult))
else:
    print("В списке не нашлось 6ти положительных элементов")
