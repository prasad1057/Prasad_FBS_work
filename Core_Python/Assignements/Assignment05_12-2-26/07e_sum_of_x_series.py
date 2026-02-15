# e. x - x2/3 + x3/5 - x4/7 + .... to n terms

x = float(input('ENter the number: '))

n = int(input('Enter the value of n: '))

total_sum = 0

for i in range(1,n+1):
    
    power = i
    denominator = (2 * i) - 1
    term = (x ** power) / denominator
    
    if i % 2 == 0:
        total_sum = total_sum - term    # if i is even then subtract from total sum
    else:
        total_sum = total_sum + term    # if i is odd then add into  total sum  
     
        
print("Sum of series =", total_sum)