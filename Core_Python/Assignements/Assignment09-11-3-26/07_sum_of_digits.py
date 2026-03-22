# 7. Write a program to find sum of digits using recursion.

def sum_of_digit(n):
    if n == 0:
        return 0
    
    else:
        return (n % 10) + sum_of_digit(n // 10)
    
n = int(input('ENter the number: '))

result = sum_of_digit(n)
print(f'Sum of digit is:{result}')