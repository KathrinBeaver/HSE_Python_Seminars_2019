# seminar 9

import datetime

myDict = {}  # или myDict = dict() - пустой словарь
myDict = {1: 2, 2: 4, 3: 9}  # статическое задание словаря
myDict = {'name': 'Jack', 'age': 20, (1, 2): 10}  # ключи могут быть любыми

myDict['age'] = 27  # обновление данных
print(myDict)  # Output: {'age': 27, 'name': 'Jack', (1, 2) : 10}

myDict['address'] = 'Novaja str.'  # добавление или обновление
print(myDict)  # Output: {(1, 2): 10, 'address': 'Novaja str.', 'age': 27, 'name': 'Jack'}

# будет ли некорректное завершение работы программы?
currentYear = datetime.datetime.today().year  # datetime - это и пакет и класс
print("%s was born in %i year" % (myDict['name'],
                                  currentYear - myDict['age']))
# а так?
# print("%s was born in %i year" % (myDict['name'],
# currentYear - myDict['SomeOtherAge'])) # KeyError!
age = currentYear - myDict.get('SomeOtherAge', -1)  # -1 значение по умолчанию, которое возвращается, если ключа нет
print("%s was born in %i year" % (myDict['name'], age))  # Почти хорошо, разве что Джек родился в будущем


myDict2 = {10:"a", 2:"b"}
print(sorted(myDict2))
for el in myDict:
    print(el)
#myDict.popitem()