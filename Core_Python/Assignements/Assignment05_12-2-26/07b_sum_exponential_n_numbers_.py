# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

num = int(input('Enter the number: '))

sum = 0

for i in range(1,num+1):
    sum = sum + (num ** i)
    
print(sum)