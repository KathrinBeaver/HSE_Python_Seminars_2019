class Tree: # объявление класса
  #  treeName = str()  # Объявление атрибута класса
    __treeName = str()  # Правильное объявление атрибута класса - private!
    # Нет особых спецификаторов для области видимости, вместо этого используется преффикс "__"

    def grow(self):  # Метод класса, self - обязательный формальный параметр для методов при их объявлении
        print("I am a(an) %s. I am growing" % self.__treeName)

    def getName(self):  # Метод для получения данных из объекта класса, "геттер" или "акцессор"
        return self.__treeName

    def setName(self, name):  # Метод для установки данных в объект класса, "сеттер" или "акцессор"
        self.__treeName = name

    def __init__(self):  # Конструктор класса
        self.__treeName = "Default Tree"

myOak = Tree()
myOak.treeName = "Oak"
myOak.__treeName = "Maple"
myOak.setName("Pine")
myOak.grow()
myOak.size = 10  # Поля к классу можно добавлять "на лету" (но ненужно)
print(myOak.size)
print(myOak.__treeName)
print(myOak.getName())

print(myOak)

