inputStr = input("Введите слово: ")
res = inputStr[:-3] + "***";
print(res)

inputStr = input("Введите строку: ")
res = ""
listOfWords = inputStr.split(' ')  # список из исходной строки, на основе разделителя.
print(listOfWords)

for str1 in listOfWords:     # применение цикла for - "для каждого" элемента
    res += ' ' + str1[:-3] + "***"
print(res)
