# 6. Write a program to print first n prime numbers.


n = int(input("Enter how many prime numbers: "))

count = 0
num = 2

while count < n:
    i = 2
    
    while i < num:
        if num % i == 0:
            break
        i += 1
    
    if i == num:
        print(num)
        count += 1
    
    num += 1
