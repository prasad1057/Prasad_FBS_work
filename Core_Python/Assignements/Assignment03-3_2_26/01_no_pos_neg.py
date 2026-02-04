# 1. Write a program to check if the given number is positive or negative.

number = int(input('Enter the number: '))

if number > 0:
    print('Number is Positive')
elif number < 0:
    print('Number is Negative.')
else:
    print('Number is zero.')