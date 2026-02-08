# 12. Write a program to check if given 3 digit number is a palindrome or not.

original_number = int(input('Enter the number to check it is pallindrome or not: '))
number = original_number            # store original value


rem1 = number % 10          # give last digit 
number = number // 10       # remainign two digits(first 2 digits)

rem2 = number % 10          # give second last digit
number = number // 10       # remaining 1 digit(first digit)

rem3 = number % 10          # last digit
number = number // 10

sum = rem1 + rem2 + rem3            # if u want sum of three digit of input

# if number is 156

rem1_digit = rem1 * 100         # 6 * 100  = 600
rem2_digit = rem2 * 10          # 5 * 10   =  50
rem3_digit = rem3 * 1           # 1 * 1    =   1         
# all of three gives reverse number 

pallindrome = rem1_digit + rem2_digit + rem3_digit          # addition of all these is 651
print("Reversed number: ", pallindrome)

if pallindrome == original_number:
    print('It is a Pallindrome')
    
else:
    print('It is not a Pallindrome')