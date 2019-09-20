text = "Строкаааа для знаний о языке"

maxWord = ""
i = 0
maxLengthOfWord = 0
while i < len(text):
    word = ""
    while i < len(text) and text[i] != ' ':
        word += text[i]
        i += 1
    if len(maxWord) < len(word):
        maxWord = word
    i += 1

print(maxWord)

i = 0
wordMaxNew = ""
while i < len(maxWord):
    if maxWord[i] == 'а':
        # нельзя word[i] = 'б'
        wordMaxNew += "б"
    else:
        wordMaxNew += maxWord[i]
    i += 1

print(wordMaxNew)

while i < len(text):
    space = text.find(' ', i)
    word = text[i:space - 1]
    if len(maxWord) < len(word):
        maxWord = word
    i += space
listOfWords = text.split()
