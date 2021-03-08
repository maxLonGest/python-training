def gcd(_a, _b):
    if _a == 0 or _b == 0:
        return _a + _b
    if _a > _b:
        _a = _a % _b
    else:
        _b = _b % _a
    return gcd(_a, _b)


a = int(input())
b = int(input())
print(gcd(a, b))
