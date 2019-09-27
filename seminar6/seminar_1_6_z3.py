# Задача 3
# Найдите все 4х значные числа, являющиеся полными квадратами. (Имеют целое значение кв. корня) Сколько их?
import math, time

# Cпособ 1
startTime = time.clock()
count = 0

for i in range(1000, 9999 + 1):
    if (math.sqrt(i).is_integer()):
        print(i, end=" ")
        count += 1
timeTaken1 = time.clock() - startTime
print("\nЗатрачено времени: %g, всего чисел %d" % (timeTaken1, count))

# Cпособ 2
startTime = time.clock()
count = 0
startNum = math.ceil(math.sqrt(1000))
finishNum = math.floor(math.sqrt(9999))

for i in range(startNum, finishNum + 1):
    print(i * i, end=" ")
    count += 1
timeTaken2 = time.clock() - startTime
print("\nЗатрачено времени: %g, всего чисел %d" % (timeTaken2, count))
print("\n\nСпособ 1 медленнее в %g раз" % (timeTaken1 / timeTaken2, ))