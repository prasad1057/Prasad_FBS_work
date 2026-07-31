# 7. Find the sum of three-digit number.

number = int(input('Enter a three-digit number: '))

# Extract last digit
d1 = number % 10
number = number // 10

# Extract middle digit
d2 = number % 10
number = number // 10

# Extract first digit
d3 = number % 10
number = number // 10

# Sum of digits
sum_of_digits = d1 + d2 + d3

print('Sum of three-digit number is:', sum_of_digits)




# sum = 0
# for i in range(1,number+1):
#     for j in i:
#         digit = number % 10
#         sum += digit
#         number = number // 10
    
# print(sum)