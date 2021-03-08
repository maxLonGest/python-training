a = int(input())
b = int(input())
c = int(input())
count = 0
if a == b:
    count = count + 1
if a == c:
    count = count + 1
if b == c:
    count = count + 1
if count == 1:
    count = count + 1
print(count)
