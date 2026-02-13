# 1. WAP to print all even numbers until n.

number = int(input('Enter the number: '))

i = 1

while(i <= number):
    if i % 2 == 0:
        print(i)
    i += 1
    