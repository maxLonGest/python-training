s = input()
negativS = s[::-1]
firstIndex = s.find('h')
lastIndex = len(s) - negativS.find('h') - 1
result = s[:firstIndex] + s[lastIndex + 1:]
print(result)
