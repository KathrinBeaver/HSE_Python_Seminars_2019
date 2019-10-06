# seminar 9

# В файле хранится гинеалогическое дерево породы собак за несколько поколений
# Формат хранения Кличка-родитель1-родитель2-возраст
# Для введенных 2х имен определить являются ли они прямыми потомками

file = open("z2.txt", 'r')
dogs = {}
for line in file.readlines():
    dogInfo = line.split("-")
    if len(dogInfo) == 4:
        dogs[dogInfo[0]] = {"parents": tuple(dogInfo[1:3]), "age": int(dogInfo[3].strip())}
print(dogs)
file.close()

# dog1 = input("Введите кличку собаки1:")
# dog2 = input("Введите кличку собаки2:")
dog1 = "Bob"
dog2 = "John"

if dog1 not in dogs:  # Проверка существования ключа
    print(dog1, "нет в списке")
    exit(0)
if dog2 not in dogs:
    print(dog2, "нет в списке")
    exit(0)
if dog2 in dogs[dog1]['parents']:
    print(dog2, "является родителем", dog1)
elif dog1 in dogs[dog2]['parents']:
    print(dog1, "является родителем", dog2)
else:
    print("Прямое родство не обнаружено")
