n = int(input())
standardSum = int(n * (n + 1) / 2)
currentSum = 0
for i in range(1, n):
    a = int(input())
    currentSum += a
print(standardSum - currentSum)
