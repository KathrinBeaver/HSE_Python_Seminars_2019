import os

path = ".\\goods"
dirFiles = os.listdir(path)
goods = set()

for fileName in dirFiles:
    if (fileName.endswith(".txt")):
        file = open(path + "\\" + fileName, "r")
        for line in file.readlines():
            goods.add(line.split(",")[0])
        file.close()
print("Найдены товары:", goods)
