'''
Write a program to find print the following Fibonacci series using
functions:
1 1 2 3 5 8 n terms
'''



# without passing parameter
# wihtout return value
def fibonacci1():
    n = int(input("Enter number: "))
    
    a = 0
    b = 0
    c = 1
    
    for i in range(1,n+1):
        a = b
        b = c
        c = a + b
        print(b, end=" ")
        
fibonacci1()



# with passing parameter
# without return value
def fibonacci2(a,b,c,n):
    
    for i in range(1,n+1):
        a = b 
        b = c
        c = a + b
        print(b,end=' ')

n = int(input("Enter number: "))
a = 0
b = 0
c = 1

fibonacci2(a,b,c,n)    
    
    

# wihtout passing parameter
# with returning value
def fibonacci3():
    n = int(input("Enter number: "))
    a = 0
    b = 0
    c = 1
    series = []
    
    for i in range(1,n+1):
        a = b
        b = c
        c = a + b
        series.append(b)        # if we want to print whole series then we have to use list 
        
    return series

result = fibonacci3()
print(result)       #print(fibonacci3())
        



# with passing parameter
# with return value
def fibonacci4(a,b,c,n,series):
    
    for i in range(1,n+1):
        a = b
        b = c
        c = a + b
        
        series.append(b)
    return series
    
n = int(input("Enter number: "))
a = 0
b = 0
c = 1
series = []

result = fibonacci4(a,b,c,n,series)
print(result)