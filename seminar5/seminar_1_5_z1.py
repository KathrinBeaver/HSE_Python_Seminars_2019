def countPercent(start, percent, n):
    sum = 0.0
    term = 1
    i = 1
    while i <= n:
        term *= 1 + percent / 100
        sum = start * term
        i += 1
    return sum

startMoney = 100.0  # float(input("Сколько было? "))
percent = 10.0  # float(input("Под какой процент? "))
years = 10  # int(input("На сколько полных лет? "))
i = 1
while (i <= years):
    print("Выплаты за %iй год %g" % (i, countPercent(startMoney, percent, i)))
    i += 1
