# seminar 6

myTuple = 10, 5  # создание кортежа
myTuple = (10, None, 5)  # лучше так
print(myTuple)
print (myTuple[0])  # обращение к элементу
print (myTuple[1:])  # срез, аналогичный строке
# myTuple[0] = 11 #  нельзя!
myTuple = tuple("Hello")  #функция tuple
myTuple1 = ("a")
print(type(myTuple1))  # кортеж???
myTuple1 = ("a",)  # кортеж!
print(type(myTuple1))
print(myTuple1 + myTuple)
print(myTuple * 3)
print(myTuple + (len(myTuple),))  # что будет напечатано?

# Только на Питоне
a = 10
b = 5
# a, b = b, a  # поменять переменные местами (А как в других языках?)
a = a + b
b = a - b
a = a - b
print(a, b)

# проверка существования элемента в кортеже
if 'e' in myTuple:
   print ("'e' exists!")
