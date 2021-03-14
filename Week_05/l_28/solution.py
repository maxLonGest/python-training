n = int(input())
a = list(map(int, input().split()))
b = []
x = int(input())
for i in range(len(a)):
    b.append(a[i] - x)
min_index = b.index(min(b, key=abs))
print(a[min_index])
