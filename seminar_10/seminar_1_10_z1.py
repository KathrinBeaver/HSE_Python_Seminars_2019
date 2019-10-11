def fibonacci(n):
   fib1, fib2 = 0, 1
   for i in range(n):
       fib1, fib2 = fib2, fib1 + fib2
       yield fib1

for fib in fibonacci(20):
   print(fib, end=' ')
print()

print('Сумма первых 100 чисел Фибоначчи равна', sum(fibonacci(100)))
print(list(fibonacci(16)))
print([x * x for x in fibonacci(14)]) # Списковое включение
