def power(_a, _n):
    if _n == 0:
        return 1
    if _n % 2 != 0:
        return _a * power(_a, _n - 1)
    return power(_a * _a, _n // 2)


a = float(input())
n = int(input())
print(power(a, n))
