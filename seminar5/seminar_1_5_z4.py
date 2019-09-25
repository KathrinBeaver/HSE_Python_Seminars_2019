def getNext(str1):
    i = 1
    retVal = ""
    if (str1[-1] != 'z'):
        return str1[:-i] + chr(ord(str1[-1]) + 1)

    while str1[-i] == 'z':
        i += 1
    if (i == len(str1) + 1): return ""  # если уже zzz

    retval = str1[:-i + 1]
    retval = getNext(retval)
    retval += 'a' * (i - 1)
    return retval

str1 = "aav"
str2 = "aba"

print(str1)
tmp = getNext(str1)
while tmp != str2:
    print(tmp)
    tmp = getNext(tmp)
print(str2)