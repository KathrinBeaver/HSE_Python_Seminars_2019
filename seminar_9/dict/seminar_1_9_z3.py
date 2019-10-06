# seminar 9

# На полках в магазине храяться различные товары.
# Полка может выдержать N кг товара (задается константой).
# Для заданных в файле товаров посчитать выдержат ли их соответствующие полки
# Формат файла "Товар: полка, количество, вес 1 упаковки"

N = 150  # вес, который полка может удержать

file = open("z3.txt", 'r')
shelves = {}

for line in file.readlines():
    if len(line.strip()) == 0:
        break
    itemInfo = line.split(":") # ["товар", "полка-количество"]
    values = itemInfo[1].split(',') # ["полка", "количество", "вес 1 штуки"]
    shelveNum = int(values[0].strip())
    if shelveNum in shelves:
        if itemInfo[0] in shelves[shelveNum]: # если такой товар на этой полке уже есть
            shelves[shelveNum][itemInfo[0]]['ammount'] += int(values[0].strip())
        else:
            shelves[shelveNum][itemInfo[0]] = {"ammount": int(values[1].strip()), "itemWeight": int(values[2].strip())}
    else:
        shelves[shelveNum] = {}
        shelves[shelveNum][itemInfo[0]] = {"ammount": int(values[1].strip()), "itemWeight": int(values[2].strip())}

print(shelves)
file.close()

for shelveNum in shelves.keys(): # keys можно не писать
    sum = 0
    for item in shelves[shelveNum]:
        sum += shelves[shelveNum][item]['itemWeight'] * shelves[shelveNum][item]['ammount']
    if sum > N:
        print("Полка номер", shelveNum, "не выдержит веса!")
