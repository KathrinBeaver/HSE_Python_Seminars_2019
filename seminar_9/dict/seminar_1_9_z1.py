# seminar 9

# Подсчитать, сколько раз употреблялись имена собственные в тексте.
# Вывести в упорядоченном от виде от большего к меньшему.
# Для простоты в тексте имена встречаются только в именительном падеже

text = "Вася Петя Петя"  # input("Введите текст:\n")
names = {}
# поиск имен и добавление в словарь
for word in text.split():
    if word[0].isupper():
        if word in names:
            names[word] += 1
        else:
            names[word] = 1
# сортировка
result = sorted(names.items(), key=lambda x: x[1], reverse=True)
print(result)  # result - список кортежей (key, value)
print()

print(sorted(names))
