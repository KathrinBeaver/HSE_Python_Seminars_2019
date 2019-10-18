# "ttt" + 5

# 100 / 0

# int("hello")

try:
    x = 100 / 0
except ZeroDivisionError:
    print("Errror: division by 0")
    x = 0

try:
    x = 100 / 0
except ArithmeticError: # FloatingPointError, OverflowError, ZeroDivisionError.
    print("Errror: division by 0")
    x = 0

print("x =", x)

file = open('1.txt')
ints = []
for line in file:
    try:
        ints.append(int(line))
    except ValueError:
        print('Это не число!')
    except Exception:
        print('Что это?')
    else:
        print('Сейчас все хорошо')
    finally:
        print('Это выполняется всегда!')

# file.close()
# print('Файл закрыт.')