# 5. Write a program to find factorial using recursion.

def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    
    elif n == 0:
        return 1
    
    else:
        return None
    
n = int(input('Enter the number: '))

result = factorial(n)
print('Factorial:',result)