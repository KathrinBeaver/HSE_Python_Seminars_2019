# Generator

def generate_squares():
   for i in (1, 2, 3):
       yield i * i

generator = generate_squares()
print("First Element", generator.__next__())
print("Others:", end=" ")
for i in generator:
   print(i, end=" ")
# print("Element:, generator.__next__()) <-- exception, генератор закончился, next уже некуда

