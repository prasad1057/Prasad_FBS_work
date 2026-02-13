# 5. WAP to print Fibonacci series upto n.

number = int(input('ENter the number: '))

a = -1
b = 1
c = 0

# while(c < number):
#     c = a + b
#     print(c,end='')
#     a = b
#     b = c


for i in range(1,number+1):
    c = a + b
    print(c,end='')
    a = b
    b = c