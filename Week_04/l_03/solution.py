import math


def distance(_x1, _y1, _x2, _y2):
    return math.sqrt((_x1 - _x2)**2 + (_y1 - _y2)**2)


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
a = distance(x1, y1, x2, y2)
b = distance(x1, y1, x3, y3)
c = distance(x2, y2, x3, y3)
print(a + b + c)
