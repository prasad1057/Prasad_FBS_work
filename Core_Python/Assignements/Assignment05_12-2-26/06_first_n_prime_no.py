# 6. Write a program to print first n prime numbers.


num = int(input("Enter how many prime numbers you want: "))

count = 0
n = 2

while count < num:      # to execute all conditons till we want
    for i in range(2,n):        # loop will check umber is prime or not if yes then break 
        if n % i == 0:
            break
    
    else:
        print(n,end=' ')            # then print that number which is prime
        count += 1          # to execute further loop till n
        
    n += 1

#----------------------------------------------------------------

num = int(input("Enter limit: "))
n = 2

for n in range(2, num + 1):
    for j in range(2, n):
        if n % j == 0:
            break
    else:
        print(n, end=" ")