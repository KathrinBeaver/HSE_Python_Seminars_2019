#Z1
a = int(input ("Введите трехзначное число: ")) # a = 543
d1 = a // 100; # d1 = 5
d2 = (a % 100) // 10 # d2 = 43 // 10 = 4
d3 = a % 10 # d3 = 3
print("Перевернули:", d3 * 100 + d2 * 10 + d1)