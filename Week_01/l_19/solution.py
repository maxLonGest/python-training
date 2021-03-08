firstHour = int(input())
firstMinute = int(input())
firstSecond = int(input())
secondHour = int(input())
secondMinute = int(input())
secondSecond = int(input())
firstMoment = firstHour * 60 * 60 + firstMinute * 60 + firstSecond
secondMoment = secondHour * 60 * 60 + secondMinute * 60 + secondSecond
print(secondMoment - firstMoment)
