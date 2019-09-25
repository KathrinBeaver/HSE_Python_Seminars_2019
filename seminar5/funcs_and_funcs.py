from math import sin, cos

def sinFunc(val):
    print("sin(" + str(val) + ") = " + str(sin(val)))

def cosFunc(val):
    print("sin(" + str(val) + ") = " + str(cos(val)))

def mathFunc(func, val):
    print("Вызов функции " + str(func))
    func(val)
    func = cosFunc
    func(val)

# sinFunc(2)
# newFunc = sinFunc
# newFunc(2)

sinFunc(2)
mathFunc(sinFunc, 2)
sinFunc(2)
