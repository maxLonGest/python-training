import math


def minDivisor(_n):
    i = 2
    m = math.sqrt(_n)
    while n % i != 0 and i < m:
        i += 1
    if i > m:
        return _n
    else:
        return i


n = int(input())
print(minDivisor(n))
