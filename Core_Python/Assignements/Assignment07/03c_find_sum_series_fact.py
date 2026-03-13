
# c. 1^1 + 2^2 + 3^3+ ...... n^n




# without passing parameter
# wihtout return value
def squareSeries1():
    n = int(input('Enter nmber:'))
    sum = 0
    
    for i in range(1,n+1):
        sum = sum + (i**i)
    print('Sum of square:',sum)

squareSeries1()


# with passing parameter
# without return value
def squareSeries2(n,sum):
    
    for i in range(1,n+1):
        sum = sum + (i**i)
    print('Sum of square:',sum)
    
n = int(input('Enter nmber:'))
sum = 0

squareSeries2(n,sum)



# wihtout passing parameter
# with returning value
def squareSeries3():
    n = int(input('Enter nmber:'))
    sum = 0
    
    for i in range(1,n+1):
        sum = sum + (i**i)
    return sum

result = squareSeries3()
print('Sum of Square:',result)      #print(squareSeries3())



# with passing parameter
# with return value
def squareSeries4(n,sum):
    
    for i in range(1,n+1):
        sum = sum + (i**i)
    return sum

n = int(input('Enter nmber:'))
sum = 0

result = squareSeries4(n,sum)
print('Sum of square',result)