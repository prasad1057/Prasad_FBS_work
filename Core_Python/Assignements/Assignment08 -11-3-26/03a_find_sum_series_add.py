'''
3. Write a program to find sum of following series using functions :
a. 1+ 2 + 3 + 4+..... + n
b. 1!+ 2! + 3! + 4!+..... + n!
c. 1^1 + 2^2 + 3^3+ ...... n^n
'''



# a. 1+ 2 + 3 + 4+..... + n


# without passing parameter
# wihtout return value
def sumSeries1():
    n = int(input('Enter nmber:'))
    sum = 0
    
    for i in range(1,n+1):
        sum = sum + i
    
    print('Sum os series is:',sum)

sumSeries1()



# with passing parameter
# without return value
def sumSeries2(sum,n):
    
    for i in range(1,n+1):
        sum = sum + i
    
    print('Sum of series:',sum)
    
n = int(input('Enter nmber:'))
sum = 0

sumSeries2(sum,n)



# wihtout passing parameter
# with returning value
def sumSeries3():
    
    n = int(input('Enter nmber:'))
    sum = 0
    
    for i in range(1,n+1):
        sum = sum + i
        
    return sum

result = sumSeries3()
print('Sum of Series:',result)



# with passing parameter
# with return value
def sumSeries4(n,sum):
    
    for i in range(1,n+1):
        sum = sum + i
    
    return sum

n = int(input('Enter nmber:'))
sum = 0

result = sumSeries4(n,sum)
print('Sum of Series:',result)