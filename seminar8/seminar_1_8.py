# seminar 7
#
# # Элементы списка не обязательно должны быть одного типа.
# lst = ['spam', 'drums', 100, 1234]
#
# # Для списка можно получить срез, объединить несколько списков и т.д.
# lst[1:3] # ['drums', 100]
#
# # Можно менять как отдельные элементы списка, так и диапазон:
# lst[3] = 'piano'
# lst[0:2] = [1, 2]
# print(lst) # [1, 2, 100, 'piano']
#
# # Вставка:
# lst[1:1] = ['guitar','microphone']
# print(lst) # [1, 'guitar', 'microphone', 2, 100, 'piano']
#
# # Можно сделать выборку из списка с определенной частотой:
# # numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# numbers = [x for x in range(10)]
# print(numbers[::4]) # [1, 5, 9]
#
# # Сравнение строк, кортежей, списков
#
# # строки сравниваются лексикографически (как в словаре)
# # для правильного сравнения строк надо их приводить к одному регистру!
# str1 = "Мама мыла раму"
# str2 = "мама мыла раму"
# print(str1 > str2) #true? false?
# print(str1 == str2) #true? false?
# print(str1.lower() == str2.lower()) #true? false?
#
# myTuple1 = (2, 6, 3)
# myTuple2 = (3, 1, 3)
# print(myTuple1 < myTuple2) # true, кортежи сравниваются поэлементно
# myTuple3 = (2, )
# print(myTuple1 < myTuple3) # false, myTuple1[0] == myTuple3[0], но myTuple1[1] > None
#
# myTuple1 = (2, 6, 3)
# myTuple2 = ("3", 1, 3)
# # print(myTuple1 < myTuple2) #ошибка
# print(tuple(map(str, myTuple1)) < tuple(map(str, myTuple2))) # true

# sort & sorted

# sorted - встроенная функция,
# не изменяет объекта,
# возвращая list - его копию
# можно применять к любым перечислимым типам

# myTuple = (26, 3, 5)
# # myTuple2 = sorted(myTuple)
# # print(type(myTuple2), myTuple2)
# # print(type(myTuple), myTuple)
# myStr = "Мой дядя самых честных правил"
# myStr2 = sorted(myStr)
# print(type(myStr2), sorted(myStr), myStr)
# # однако
# # myList3 = [26, 3, 5, "в", "аа"]
# # # ошибка
# # sorted(myList3)
# myList1 = myStr.lower().split()
# # # myList4 = list(map(lower, list1))
# print(sorted(myList1, reverse=True))

# # .sort() -метод у объекта, изменяет его
#
# myTuple = (26, 3, 5)
# # # нельзя кортеж-неизменяемый объект
# # myTuple.sort()
#
# myList = list(myTuple)
# myList.sort()
# print(myList)
# print(myTuple)

# # Параметры при сортировке
# ?print(sorted("This is a test string in Python".split(),
#              key=str.lower))
# # ['a', 'in', 'is', 'Python', 'string', 'test', 'This']
# print(sorted("This is a test string in Python".split()))
# #['Python', 'This', 'a', 'in', 'is', 'string', 'test']
#
# #Что будет выведено в результате выполнения сортировки?
mylist = [3, 6, 3, 2, 4, 8, 9]
print(sorted(mylist, key=lambda x: max(mylist) + x if not x % 2 else x))