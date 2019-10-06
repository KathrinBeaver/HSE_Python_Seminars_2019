# Студенты выбирают для себя предметы по выбору из списка. Выбрать нужно хотя бы один.
# По очереди они вводят в консоль свою фамилию
# Программа отображает список предметов, затем студент вводит строку с названием предмета.
# Если неверно, то надо повторить, окончание ввода  - пустая строка.

# Программа должна рассчитать:
# 1. На какой предмет записалось больше всего студентов?
# 2. Какие предметы остались не заняты?
# На какие предметы записался хотя бы один студент?
# 3. Есть ли предметы, на которые записались все? (Программирование?)
# 4. Есть ли студенты с одинаковым набором предметов?

subjectsList = ["maths", "programming", "biology", "physics"]
studentsList = []
listOfChosenSubjects = []

# Ввод и проверка данных
while True:
    surname = input("Enter your surname: ")
    if surname in studentsList:
        print("You have already chosen your subjects!")
        continue
    if surname == "": break
    studentsList.append(surname)
    listOfChosenSubjects.append(set())
    print("Hello,", surname)
    while True:
        print("Here is the list of subjects. Which one would you choose? ", end="")
        print(subjectsList)
        subject = input()

        if subject == "":
            if len(listOfChosenSubjects[-1]) == 0:  # надо выбрать хотя бы один предмет
                print("At least one subject should be chosen!")
                continue
            else:
                break
        elif subject not in subjectsList:
            print("You should enter a subject from the list")
            continue
        listOfChosenSubjects[-1].add(subject)
    listOfChosenSubjects[-1] = frozenset(listOfChosenSubjects[-1])

print(listOfChosenSubjects)

# 1
topList = [0] * len(subjectsList);

for studentChoice in listOfChosenSubjects:
    for subject in studentChoice:
        topList[subjectsList.index(subject)] += 1
print("Most interesting subject is", subjectsList[topList.index(max(topList))])

# 2
unOccupiedSubjects = set(subjectsList.copy())
for studentChoice in listOfChosenSubjects:
    unOccupiedSubjects -= studentChoice
print("Nobody has chosen:", unOccupiedSubjects)
print("At least one student has chosen:", set(subjectsList) - unOccupiedSubjects)

# 3
allStudentsTaken = set(subjectsList.copy())
for studentChoice in listOfChosenSubjects:
    allStudentsTaken &= studentChoice
print("All Students Taken: ", allStudentsTaken)

# 4.1
haveSameChoice = False
for i in range(len(listOfChosenSubjects)):
    for j in range(i + 1, len(listOfChosenSubjects)):
        if listOfChosenSubjects[i] == listOfChosenSubjects[j]:
            haveSameChoice = True
            break

print("Are there 2 or more students with the same interests? -", haveSameChoice, sep="")

# 4.2
print(len(listOfChosenSubjects) != len(set(listOfChosenSubjects)))
