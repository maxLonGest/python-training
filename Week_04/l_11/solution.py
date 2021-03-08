def power(_a, _n):
    if _n == 0:
        return 1
    return _a * power(_a, _n - 1)


a = float(input())
n = int(input())
print(power(a, n))
