# seminar 3

from math import floor, ceil

a = 0.3
print(a)
print('{0:.18}'.format(a))
print('{0:.17}'.format(a))

a = 0.1
print(a)
print('{0:.18}'.format(a))
print('{0:.17}'.format(a))

if 1.0 + 2.0 == 3.0:
    print('Right');
else:
    print('Not right');

if 0.1 + 0.2 == 0.3:
    print('Right');
else:
    print('Not right');

print(0.1 + 0.2)

# Сравнение с заданной точностью
x = 0.1  # float(input())
y = 0.2  # float(input())
z = 0.3  # float(input())

eps = 1.0 * 10**-5

if abs(x + y - z) < eps:
    print('Right')
else:
    print('Not right')

# Округление
print(int(1.5))
print(round(1.5))
print(round(2.5))
print(floor(1.5))
print(ceil(1.5))

print(int(-1.5))
print(round(-1.5))
print(round(-2.5))
print(floor(-1.5))
print(ceil(-1.5))

# Работа со строками, пример
str1 = "012345678"
print(str1[-1:2:-1])  # 876543
print(str1[-1:1:-1])  # 8765432
print(str1[-1:0:-1])  # 87654321
print(str1[-1::-1])   # 876543210

# str2[0] = "!"
text = "Мой дядя самых честных правил.."
print(text.find("дядя"))  # 4  - позиция самого левого входжения подстроки в строку
print(text.rfind("я"))  # 7  - позиция самого правого входжения подстроки в строку
print(text.find("дядя", 5))  # -1 - не найдена подстрока, если начинать с 5й позиции

print(text.replace("дядя", "тетя"))  # Мой тетя самых честных правил..
print(text.replace("Вася", "Петя"))  # ???

text = "   aaa   "
text.lstrip()
# text.rstrip()
# text.strip()
print(text)

text = "___aaaa___"
print(text.strip('_'))  # aaaa
