# 5. Write a program to print prime numbers between 1 to 100.


num = int(input('Enter the number till prime number you want to print: '))

for n in range(2,num):        # if u want to print multiple numbers then this loop is required
    for i in range(2,n):          # normal logic to print prime number
        if (n % i) == 0:
            #print(f'{num} is not a prime number')
            break
        
    else:
        #print(f'{num} is a prime number')
        print(n)                  # to print that all prime numbers 
