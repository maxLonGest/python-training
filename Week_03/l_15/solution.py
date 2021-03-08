s = input()
negativS = s[::-1]
firstIndex = s.find('f')
lastIndex = len(s) - negativS.find('f') - 1
if firstIndex == lastIndex:
    print(firstIndex)
elif firstIndex == -1:
    print('')
else:
    print(firstIndex, lastIndex)
