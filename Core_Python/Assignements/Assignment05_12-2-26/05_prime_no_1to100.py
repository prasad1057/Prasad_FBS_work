# 5. Write a program to print prime numbers between 1 to 100.

number = int(input('Enter the number: '))

count = 0

for i in range(1,101):
    if number % i == 0:
        count += 1

if count == 2:
    print(f'{number} is a Prime Number')
else:
    print(f'{number} is not Prime number')
        