def gcd(_a, _b):
    if _a == 0 or _b == 0:
        return _a + _b
    if _a > _b:
        _a = _a % _b
    else:
        _b = _b % _a
    return gcd(_a, _b)


def ReduceFraction(_n, _m):
    return _n // gcd(_n, _m), _m // gcd(_n, _m)


a = int(input())
b = int(input())
print(*ReduceFraction(a, b))
