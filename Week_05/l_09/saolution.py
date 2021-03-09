a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
count = 0
for x in range(0, 1001):
    if x - e != 0:
        y = (a * x ** 3 + b * x ** 2 + c * x + d) / (x - e)
    if y == 0:
        print(x, end=' ')
        count += 1
print()
print(count)
