class Engine:
    def __init__(self):  # конструктор по умолчанию
        self.__producer = ""
        self.__model = ""
        self.__tankSize = 0
        self.__fuelConsumption = 0

    def __init__(self, *values):  # конструктор "общего" вида
        if (len(values) == 4):
            self.__producer, self.__model, self.__tankSize, self.__fuelConsumption = values

    def getInfo(self):  # получить нформацию об объекте класса
        return "Procucer: %s - Model: %s - Tank size: %s - Fuel consumption: %s" % \
               (self.__producer, self.__model, self.__tankSize, self.__fuelConsumption)

    def getTankSize(self):  # get-set
        return int(self.__tankSize)

    def getConsumption(self):  # get-set
        return int(self.__fuelConsumption)

    def getTankSize(self):  # get-set
        return int(self.__tankSize)

    def setTankSize(self, newsize):  # get-set
        if 'int' in type(newsize) and newsize > 0:
            self.__tankSize = newsize


en1 = Engine("Volvo", "z35", "100", "15")
en2 = Engine("Saab", "cvt", "200", "20")
en3 = Engine("Suzuki", "250", "20", "2")
en4 = Engine("Toyota", "zFirst", "500", "20")
en5 = Engine("GMC", "gm11", "600", "70")

listOfEngines = [en1, en2, en3, en4, en5]
print(listOfEngines)  # что будет напечатано?
print(*map(lambda x: x.getInfo(), listOfEngines), sep="\n")

for engine in listOfEngines:
    print(round(engine.getTankSize() / engine.getConsumption(), 2), end=" ")
print()
# или тоже самое в одну строку
print(*(map(lambda x: round(x.getTankSize() / x.getConsumption(), 2), listOfEngines)))
