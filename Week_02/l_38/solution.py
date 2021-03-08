n = int(input())
maxSeq = n
i = 1
while n != 0:
    n = int(input())
    if n != 0 and i == 1:
        maxSeqOld = n
        i += 1
    if n > maxSeqOld and n < maxSeq:
        maxSeqOld = n
    if n != 0 and n >= maxSeq:
        maxSeqOld = maxSeq
        maxSeq = n
print(maxSeqOld)
