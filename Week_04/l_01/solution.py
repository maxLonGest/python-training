def min4(num1, num2, num3, num4):
    return min(min(num1, num2), min(num3, num4))


a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min4(a, b, c, d))
