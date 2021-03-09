n = int(input())
a = 10 ** (n - 1)
b = 10 ** n
for i in range(b - 1, a - 1, -2):
    print(i, end=' ')
