'''
2. Write a program to accept 3 digit number. If first digit is double of second 
digit and half of third digit then display "Yes, you have done it", otherwise 
display "Please try next time".

Eg :- 428 , 214 etc.
'''

# first digit = double of second
# first digit = half of third

# first you have to separate digits then give condition to them

num = int(input('Enter the number: '))          # 428

first_digit = num // 100            # give first digit n//10 = 42  --> n//100 = 4
second_digit = (num // 10) % 10     # give n//10 = 42       --> 42 % 2 = 2
third_digit = num % 10              # give 428 % 10 = 8

if (first_digit == (second_digit * 2)) and (first_digit == (third_digit // 2)):
    print('Yes, you have done it')
else:
    print('Please try next time')