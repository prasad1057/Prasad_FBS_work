# 1. Write a program to accept year from user and check if it is leap year or not.

year = int(input('Enter the year to check if it is leap year or not: '))

if year > 0:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
        print(f'{year} is a leap year')
    else:
        print(f'{year} is not leap year')
else:
    print('Please enter the correct year')
            