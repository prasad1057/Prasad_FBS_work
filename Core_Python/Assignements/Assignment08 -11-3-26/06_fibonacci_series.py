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
    b = 1
    
    #series=[]
    
    for i in range(1,n+1):
        c = a+b
        print(c,end=' ')
        a = b
        b = c
    
fibonacci1()



# with passing parameter
# without return value
def fibonacci2(n):
    
    a = 0
    b = 1
    
    #series=[]
    
    for i in range(1,n+1):
        c = a+b
        print(c,end=' ')
        a = b
        b = c

n = int(input("Enter number: "))
fibonacci2(n)    
    
    

# wihtout passing parameter
# with returning value
def fibonacci3():
    n = int(input("Enter number: "))
    a = 0
    b = 1
    
    series=[]
    
    for i in range(1,n+1):
        c = a+b
        series.append(c)
        a = b
        b = c
    return series

result = fibonacci3()
print(result)       #print(fibonacci3())
        



# with passing parameter
# with return value
def fibo(n):
    
    a = 0
    b = 1
    
    series=[]
    
    for i in range(1,n+1):
        c = a+b
        series.append(c)
        a = b
        b = c
    return series
    
n = int(input('enter: '))
print(fibo(n))  