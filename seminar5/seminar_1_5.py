from math import sin

def myFunc(str1):  # str1 - обязательный параметр
    """            # описание функции (опционально)
    Эта функция делает много полезного
    :param str1: один входной параметр
    :return: возвращает строку наоборот
    """
    str2 = ""
    i = 1
    while (len(str2) < len(str1)):
        str2 += str1[-i]
        i += 1
    str1 = "AAA"
    print("id str1 =", id(str1))
    return str2  # возвращаемое значение (опционально)

def sinFunc(val):
    print("sin(" + str(val) + ") = " + str(sin(val)))

def mathFunc(func, val):
    print("Вызов функции " + str(func))
    func(val)

testStr = "Hello!"
# print(myFunc.__doc__)
# help(myFunc)
# print(testStr, id(testStr))
# print(myFunc(testStr))
# print(testStr, id(testStr))

newFunc = myFunc  # имя функции - самостоятельная переменная-ссылка, её тоже можно присваивать
#print(newFunc("Еще одна строка"))

#sinFunc(2)
#mathFunc(sinFunc, 2)

def get_person_info(name, age):  # Порядок вывоза важен, get_person_info (23, "Ivan") - некорректно
    print(name, "is", age, "years old")

# get_person_info (23, "Ivan")
# Хотя в описании функции первым аргументом идет имя, мы можем вызвать функцию вот так
# get_person_info(age=23, name="John")

def empty(agr1=30):  # аргументы могут задаваться параметрами по умолчанию
    # print(agr1)
    pass  # можно использовать когда функция не готова, но требуется ее объявить

# print(empty())  # None, т.к. функция ничего не возвращает

if empty() is not None:
    print("not None")
else:
    print("None")

func = lambda x, y: x + y  # функции могут быть анонимными
func(1, 2)  # при этом они остаются функциями
func('a', 'b')  # не строгая типизация, это плюс и минус
# func (1, 'a')             # а вот это уже ошибка! Нельзя складывать int и string
(lambda x, y: x + y)(1, 2)  # можно объединять объявление и вызов анонимной функции

def fact(n):
    return 1 if n == 1 else fact(n-1) * n

# print("10! =", fact(10)) # 10! = 3628800

b1 = 1
def geomProgr(n, q):
    return n if n == b1 else geomProgr(n-1, q) * q

# print("B5 =", geomProgr(5, 2))  # B5 = 16