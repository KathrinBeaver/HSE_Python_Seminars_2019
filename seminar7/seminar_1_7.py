# seminar 6

import copy

# myList = ['a', 10]
# print(*myList)

# myList[-1] = 20
# print(myList)
# print("В обратном порядке:", myList[::-1])
#
# myList = [1, 2]
# print("MyList size:", myList.__sizeof__())
# print("MyList elements count:", myList.__len__())
# print("MyList elements count:", len(myList))
#
# myTuple = (1, 2)
# print("MyTuple size:", myTuple.__sizeof__())
# print("MyTuple elements count:", myTuple.__len__())
# print("MyTuple elements count:", len(myTuple))

# lst = list()
# tpl = tuple()
#
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# words = ["dog", "frog", "cat", "tiger"]
# if 'cat' in words:  # not in
#     print('yes')

# Копирование списков - shallow copy - ТОЛЬКО ссылки!
# myList1 = [10, 12]
# myList2 = myList1
# myList1[0] = 11
# print(myList2)  # что будет выведено?
#
# myList2 = myList1.copy()  # copy (1 уровень), deep copy - copy.deepcopy(myList1)
# myList1[0] = 100500
# print(myList2)  # что будет выведено?

myList1 = [111, 222]
myList2 = [333, 444]

# myList3 = [myList1, myList2]
# print(myList3)
# myList4 = myList3.copy()  # что скопируется?? списки? ссылки?
# # myList4 = copy.deepcopy(myList3) #что скопируется?? списки? ссылки?
# print("*****")
# print(myList4)
# myList1[0] = 0
# myList2[0] = 1
# print(myList4)
# print("*****")

# # но если вот так, то будут новые объекты!
# myList3 = [myList1, myList2]
# print(myList3)
# myList4 = myList3.copy()  # что скопируется?? списки? ссылки?
# myList1 = [1, 1]
# myList2 = [1, 1]
# print(myList4)

# #split
# print("Введите последовательность чисел через пробел: ")
# numbers = [int(s) for s in input().split()]
# print(numbers)

# str3 = "aa bb ss ff"
# print(str3.split(" ", 2))

# # join
# words = ["cat, dog, frog, tiger"]
# st = ", ".join(words)  # Строка "dog, frog, cat, tiger"
# print(st)
#
# numbers = [1, 2, 3, 4, 5, 3, 1]
# # st1 = ' '.join(numbers)    # Почему так нельзя?
# st1 = ' '.join(map(str, numbers))  # 1 2 3 4 5 3 1
# print(st1)

# numbersList = list(map(str, numbers))
# st2 = ' - '.join(numbersList)  # 1 - 2 - 3 - 4 - 5 - 3 - 1
# print(st2)
#
# map
# words = ["dog", "frog", "cat", "tiger"]
# print(list(map(len, words)))  # [3, 4, 3, 5]
#
# print(list(map(lambda x, y: x * y, [1, 2], [3, 4, 5])))  # [3, 8]
#
# # zip
# a = [1, 2]
# b = [3, 4]
# print(list(zip(a, b)))  # [(1, 3), (2, 4)]
#
# insert list list
lst = [1, 2]
print(lst)
lst[1:1] = [3, 4]
# lst.insert(1, [3, 4])
print(lst)
