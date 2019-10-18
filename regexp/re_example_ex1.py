import re

testStr1 = input('Введите строку для поиска:')
result = re.findall(r'\s?\d+\s?', testStr1)
print(result)

emailList = ['ssss@yandex.ru', 'test1@google.com', 'rrrrr@google.com', 'test12345@google.com']

for email in emailList:
    if re.match(r'[a-z0-9,.-]{5}@google.com', email):
        print('yes')
    else:
        print('no')
