# prime number

num = int(input('Enter the number to check prime or not: '))

for i in range(2,num):
    if (num % i) == 0:
        print(f'{num} is not a prime number')
        break

else:
    print(f'{num} is a prime number')