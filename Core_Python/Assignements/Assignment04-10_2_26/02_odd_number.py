# 2. WAP to print all odd numbers until n.

number = int(input('Enter the number: '))

num = 0

while(num <= number):
    if num % 2 != 0:
        print(num)
    num = num + 1