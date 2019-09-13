# seminar 2

a = 5     # 0b101
b = 6     # 0b110

c = a & b # 0b100 == 4
d = a | b # 0b111 == 7
e = a ^ b # 0b011 == 3
f =  ~ a  # 0b1...11111010 == -6

print(bool(a >> 3))         # сдвиг вправо(деление на 2^k)
print(bool(a << 3))         # сдвиг влево (умножение на 2^k)
print(bool(a) != bool(b))   # logic xor

print("\nTrue or false?")
print(bool('0'))
print(bool('False'))
print(bool('false'))
print(bool(0))
print(bool(0.0))
print(bool(' '))
print(bool(''))

a = 0
b = 0
c = 0

# 1
if a > 0:
    b = 10
    c = 20

# 1a
if (not a): b = 0

# 2
if a > b > c:
    b = 10
    c = 20
else:
    b = 20
    c = 10

# 3
if ~a and ~b:
    c = 10
elif (a > 10) and (b > 0):
    a = 10
else:
    a = 0

# 3a
if ~a ^ ~b:
    c = 10
else :
    if (a > 10) and (b > 0):
        a = 10
    else:
        a = 0
        print ("Внутри else")
print("Вне блоков")

str1 = "-8"
a = "-8".lstrip("-").isdigit()
print(a)

import re
_float_regexp = re.compile(r"^[-+]?(?:\b[0-9]+(?:\.[0-9]*)?|\.[0-9]+\b)(?:[eE][-+]?[0-9]+\b)?$").match
def is_float_re(str):
    return True if _float_regexp(str) else False

int("0b11111", 2)
int("11111", 2)
int('0o37', 8)
int('37', 8)
int('0x1f', 16)
int('1f', 16)

count = 0
while (count < 9):                  # условие продолжения
   print('The count is:', count)    # тело цикла
   count = count + 1                # всё еще тело цикла