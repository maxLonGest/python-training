firstHor = int(input())
firstVer = int(input())
secondHor = int(input())
secondVer = int(input())
if ((firstHor + firstVer) % 2) == ((secondVer + secondHor) % 2):
    print('YES')
else:
    print("NO")
