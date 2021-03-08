startHor = int(input())
startVer = int(input())
endHor = int(input())
endVer = int(input())
if (-1 <= startVer - endVer <= 1) and (-1 <= startHor - endHor <= 1):
    print('YES')
else:
    print('NO')
