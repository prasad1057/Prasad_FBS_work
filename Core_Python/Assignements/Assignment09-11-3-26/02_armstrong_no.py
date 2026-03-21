# 2. Write a program to check if given number is Armstrong or not using recursive function.

def armstrong(n,count):
    if n == 0:
        return 0
    
    digit = n % 10
    return (digit ** count) + armstrong(n//10, count)

n = int(input('Enter the number: '))

count = len(str(n))

result = armstrong(n,count)

if result == n:
    print(f'{n} is Armstrong number')
else:
    print(f'{n} is not armstrong number')