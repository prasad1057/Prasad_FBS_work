# Fibonacci series

n = int(input('Enter the number: '))

a = -1
b = 1

for i in range(n):
    c = a + b           # c = addition of previos two values
    print(c,end='')
    a = b               # store previuos value in b
    b = c               