import math
import random
length = 100
lst = [random.randrange(1, 100) for x in range(length)]
print(lst)
numberOfSquares = len(list(filter(lambda x: math.sqrt(x).is_integer(), lst)))
percentOfSquares = round(numberOfSquares / len(lst) * 100)
print("Процент полных квадратов в последновательности равен %d" % percentOfSquares)

# тоже самое в 1 строку
percentOfSquares = round(len(list(filter(lambda x: math.sqrt(x).is_integer(), [random.randrange(1,100) for x in range(length)]))) / length * 100)
print("Процент полных квадратов в последновательности равен %d" % percentOfSquares)
