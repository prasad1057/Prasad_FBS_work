# 3. WAP to print sum of series upto n.

number = int(input('Enter the number: '))
i = 0
sum = 0

while(i <= number):
    sum = sum + i
    i = i + 1
print('Sum of series of n number: ',sum)