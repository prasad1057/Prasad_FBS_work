# fibonacci

num = int(input('Enter the number: '))
a = -1
b = 1

for i in range(num):
    c = a + b
    print(c,end='')
    a = b
    b = c