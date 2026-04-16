# 4. Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).



num = int(input('Enter value of n: '))

result = {}

for x in range(1, num+1):
    result[x] = x*x
    
print(result)