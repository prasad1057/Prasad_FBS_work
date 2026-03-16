# 5. Sum of all prime numbers between 1 to n




# without passing parameter
# wihtout return value
def sumEven1():
    n = int(input('Enter nmber:'))
    sum = 0
    
    for i in range(1,n+1):
        if (i % 2) == 0:
            sum += i
    print('Sum of even numbers:',sum)
    
sumEven1()


# with passing parameter
# without return value
def sumEven2(n,sum):
    
    for i in range(1,n+1):
        if (i % 2) == 0:
            sum += i
    print('Sum of even numbers:',sum)
    
n = int(input('Enter nmber:'))
sum = 0

sumEven2(n,sum)


# wihtout passing parameter
# with returning value
def sumEven3():
    n = int(input('Enter nmber:'))
    sum = 0
    
    for i in range(1,n+1):
        if (i % 2) == 0:
            sum += i
    return sum

result = sumEven3()
print('Sum of even numbers:',result)


# with passing parameter
# with return value
def sumEven3(n,sum):
    
    for i in range(1,n+1):
        if (i % 2) == 0:
            sum += i
    return sum

n = int(input('Enter nmber:'))
sum = 0

result = sumEven3(n,sum)
print('Sum of even numbers:',result)