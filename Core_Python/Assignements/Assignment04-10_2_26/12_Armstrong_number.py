'''
12. Write a program to check if given number is Armstrong number or not.
(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)
'''

# number = int(input('Enter the number: '))
# original_number = number

# count = len(str(number))
# sum = 0

# while(number > 0):
#     digit = number % 10
#     sum += digit ** count
#     number = number // 10
    
# if original_number == sum:
#     print(f'{original_number} is Armstrong number.')
# else:
#     print(f'{original_number} is not Armstrong number.')
# #print(sum)





number = int(input('Enter the number: '))
original_number = number

# Step 1: count digits
count = 0
temp = number

while temp > 0:
    count += 1
    temp = temp // 10

# Step 2: calculate sum
sum = 0
temp = number

while temp > 0:
    digit = temp % 10
    sum += digit ** count
    temp = temp // 10

# Step 3: check
if original_number == sum:
    print(f'{original_number} is Armstrong number.')
else:
    print(f'{original_number} is not Armstrong number.')