a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c
if d >= 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    if x1 == x2:
        print(x1)
    else:
        print(min(x1, x2), max(x1, x2))
else:
    print()
