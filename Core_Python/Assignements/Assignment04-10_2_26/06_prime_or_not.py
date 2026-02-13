# 6. WAP to check if a given number is prime number or not.

number = int(input('ENter the number: '))

# i = 1
count = 0

# while i <= number:
#     if number % i == 0:
#         count += 1
#     i += 1
    
# if count == 2:          # count will increase if number divisible is 1 and self
#     print(f'{number} is Prime Number')
# else:
#     print(f'{number} is not Prime Number.')


for i in range(1,number+1):
    if number % i == 0:
        count += 1
        
if count == 2:
    print(f'{number} is a prime number')

else:
    print(f'{number} is not a prime number')