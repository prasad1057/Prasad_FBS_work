# 9. WAP to print all numbers in a range divisible by a given number.

'''
Suppose:

Range: 1 to 20
Given number: 4

Numbers divisible by 4:
4, 8, 12, 16, 20
'''

number = int(input('Enter the starting number: '))
ending_number = int(input('Enter the ending number: '))

divisor = int(input('Enter the number that will divide all numbers: '))


while(number <= ending_number):
    if number % divisor == 0:
        print(number)
    number += 1