s = input()
index = s.find(' ')
result = s[index + 1:] + ' ' + s[:index]
print(result)
