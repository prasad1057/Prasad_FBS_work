# 10. WAP to check if given number is Perfect Number.

'''
A Perfect Number is a number whose:
Sum of its proper divisors = the number itself

🧩 Example 1 → Number = 6
Divisors of 6:
1, 2, 3, 6
Proper divisors (excluding 6):
1, 2, 3
Sum:
1 + 2 + 3 = 6
✅ 6 is a Perfect Number
'''

number = int(input('Enter the number: '))

sum = 0
i = 1

while(i < number):
    if number % i == 0:
        sum += i
    i += 1
        
if sum == number:
    print(f'{number} is a perfect number')
else:
    print(f'{number} is not a perfect number')