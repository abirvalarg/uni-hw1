#!/usr/bin/python
number = int(input('> '))

while number > 9:
    numberSum = 0
    while number > 0:
        numberSum += number % 10
        number //= 10
    number = numberSum
print(number)
