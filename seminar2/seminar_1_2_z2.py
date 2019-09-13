import math

rad_str = input("Введите радиус: ")

if (rad_str.isdigit()):
    rad = int(rad_str)
else:
    exit(1)

print("P окружности равен ", 2 * math.pi * rad, sep ='')
print("S круга равна", rad * math.pi ** 2 / 2) # у возведения в степень приоритет выше