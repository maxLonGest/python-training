n = int(input())
maxSeq = n
countMax = 1
while n != 0:
    n = int(input())
    if n == maxSeq:
        countMax += 1
    if n > maxSeq:
        maxSeq = n
        countMax = 1
print(countMax)
