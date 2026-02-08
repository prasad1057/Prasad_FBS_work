# 12. Write a program to check if given 3 digit number is a palindrome or not.

number = int(input('Enter the number to check it is pallindrome or not: '))

rem1 = number % 10          # give last digit 
number = number // 10       # remainign two digits(first 2 digits)

rem2 = number % 10          # give second last digit
number = number // 10       # remaining 1 digit(first digit)

rem3 = number % 10          # last digit
number = number // 10

sum = rem1 + rem2 + rem3

rem1_digit = rem1 * 100
rem2_digit = rem2 * 10
rem3_digit = rem3 * 1

pallindrome = rem1_digit + rem2_digit + rem3_digit

print('THis is the pallindorme of number', pallindrome)