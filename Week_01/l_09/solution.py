number = int(input())
sum = 0
sum = sum + number % 10
number = number // 10
sum = sum + number % 10
number = number // 10
sum = sum + number % 10
number = number // 10
print(sum)
