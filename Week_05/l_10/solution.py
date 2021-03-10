def factorial(_n):
    if _n == 1:
        return 1
    return _n * factorial(_n - 1)


n = int(input())
summa = 0
for i in range(1, n + 1):
    summa += factorial(i)
print(summa)
