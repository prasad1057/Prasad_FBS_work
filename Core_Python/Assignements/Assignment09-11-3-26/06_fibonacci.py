# 6. Write a program to print Fibonacci series using recursion.

# F(n) = F(n−1) + F(n−2)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input('Enter the number: '))

for i in range(n):
    print(fibonacci(i),end=' ')