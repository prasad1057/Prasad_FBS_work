
# a. 1! + 2! + 3! + 4! + .....n!

num = int(input('Enter the number till which u want factorial: '))

sum = 0

for i in range(1,num+1):        # this loop runs from 1 to n
    
    fact = 1
    
    for j in range(1,i+1):      # actually calculate the factorial of each number
        fact = fact * j
        
    sum += fact
    
print('Sum of factorial are: ',sum)