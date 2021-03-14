a = list(map(int, input().split()))
for i in range(len(a)):
    if i % 2 != 0:
        a[i], a[i - 1] = a[i - 1], a[i]
print(*a)
