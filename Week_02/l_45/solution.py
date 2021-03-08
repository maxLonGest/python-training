n = int(input())
maxSeq = 1
curSeq = 1
prevN = n
while n != 0:
    n = int(input())
    if n == prevN:
        curSeq += 1
    else:
        if curSeq > maxSeq:
            maxSeq = curSeq
        curSeq = 1
    prevN = n
print(maxSeq)
