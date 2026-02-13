# 2. WAP to print all odd numbers until n.

number = int(input('Enter the number: '))

# num = 0

# while(num <= number):
#     if num % 2 != 0:
#         print(num)
#     num = num + 1


for i in range(1,number+1):
    if i % 2 != 0:
        print(i)