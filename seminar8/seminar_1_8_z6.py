# Задача 6
# Прочитать из файла список скачиваний файлов за неделю (Формат: <имя файла> <номер недели> <количество>.
# Вывести в output.txt все файлы в алфавитном порядке без повторов с суммарном количеством скачиваний.
# Рассчитать самую загруженную неделю

names = [] # имена файлов
downloads = [] # количество скачиваний
weeks = [] # номера недель
downloadsByWeeks = [] # количество скачиваний

file = open('input.txt', 'r', encoding='utf-8')

for line in file.readlines():
    if len(line.strip()): #если не пустая строка
        values = line.split()
        if values[0] in names:
            downloads[names.index(values[0])] += int(values[2])
        else:
            names.append(values[0])
            downloads.append(int(values[2]))

        if values[1] in weeks:
            downloadsByWeeks[weeks.index(values[1])] += int(values[2])
        else:
            weeks.append(values[1])
            downloadsByWeeks.append(int(values[2]))
file.close()

print ("Самая нагруженная неделя: %s, количество скачиваний %d" %
       (weeks[downloadsByWeeks.index(max(downloadsByWeeks))], max(downloadsByWeeks)))
namesSorted = sorted(names)

file2 = open('output.txt', 'w', encoding='utf-8')
for name in namesSorted:
    file2.write("%s %d\n" % (name, downloads[names.index(name)]))
file2.close()