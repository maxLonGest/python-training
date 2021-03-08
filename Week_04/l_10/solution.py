import math


def IsPrime(_n):
    i = 2
    m = math.sqrt(_n)
    while n % i != 0 and i < m:
        i += 1
    if i > m:
        return 'YES'
    else:
        return 'NO'


n = int(input())
print(IsPrime(n))
