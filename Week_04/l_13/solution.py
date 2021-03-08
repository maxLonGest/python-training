def sum(_a, _b):
    if _b == 0:
        return _a
    _a += 1
    return sum(_a, _b - 1)


a = int(input())
b = int(input())
print(sum(a, b))
