# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.

'''
If n = 5
1
1×2 = 2
2×2 = 4
4×2 = 8
8×2 = 16

1 + 2 + 4 + 8 + 16
sum = 31
'''


num = int(input('Enter the number: '))

total = 0
term = 1

for i in range(1,num+1):
    total += term     # 0 1 3 
    term = term * 2  # 2 6

print("Sum of series is:", total)
    
