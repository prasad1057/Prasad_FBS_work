# 6. Write a program to print first n prime numbers.


num = int(input("Enter how many prime numbers you want: "))

count = 0
n = 2

while count < num:
    for i in range(2,n):
        if n % i == 0:
            break
    
    else:
        print(n)
        count += 1
        
    n += 1
        
