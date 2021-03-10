BEGIN_RANGE = 0
END_RANGE = 1000


def equation(_a, _b, _c, _d, _e, _x):
    if x - e != 0:
        return (_a * _x ** 3 + _b * _x ** 2 + _c * _x + _d) / (_x - _e)
    return 1


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
count = 0
for x in range(BEGIN_RANGE, END_RANGE + 1):
    if equation(a, b, c, d, e, x) == 0:
        count += 1
print(count)
