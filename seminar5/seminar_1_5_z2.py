def countAbs(str1, sym):
    i = 0
    count = 0
    while i < len(str1):
        if (str1[i] == sym):
            count += 1
        i += 1
    return count

#strInput = "asdqwe" 
strInput = input("Введите строку: ")

i = 0
while i < len(strInput):
        symb = strInput[i]
        absFreq = countAbs(strInput, symb)
        absFreq1 = strInput.count(symb)
        print("Symbol %c, abs_count = %i %i rel_count=%g" % (symb, absFreq, absFreq1, absFreq / len(strInput)))
        i += 1
