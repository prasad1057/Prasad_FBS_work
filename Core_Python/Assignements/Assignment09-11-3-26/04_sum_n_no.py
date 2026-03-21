# 4. Write a program to find sum of n numbers using recursion.

def sum_of_series(n):
    if n > 0:
        return n + sum_of_series(n-1)
    elif n == 0:
        return 0
    else:
        return None
    
n = int(input('Enter the number: '))

result = sum_of_series(n)
print('Sum of Series:',result)