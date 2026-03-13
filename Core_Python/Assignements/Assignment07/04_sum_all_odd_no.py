# 4. Sum of all odd numbers between 1 to n



# without passing parameter
# wihtout return value
def sumOdd1():
    n = int(input('Enter nmber:'))
    sum = 0
    
    for i in range(1,n+1):
        if (i % 2) != 0:
            sum += i
    print('Sum of odd number:',sum)

sumOdd1()



# with passing parameter
# without return value
def sumOdd2(n,sum):
    
    for i in range(1,n+1):
        if (i % 2) != 0:
            sum += i
    print('Sum of odd number:',sum)

n = int(input('Enter nmber:'))
sum = 0

sumOdd2(n,sum)




# wihtout passing parameter
# with returning value
def sumOdd3():
    n = int(input('Enter nmber:'))
    sum = 0
    
    for i in range(1,n+1):
        if (i % 2) != 0:
            sum += i
    return sum

result = sumOdd3()
print('Sum of odd number:',result)      #print(sumOdd3())



# with passing parameter
# with return value
def sumOdd4(n,sum):
    n = int(input('Enter nmber:'))
    sum = 0
    
    for i in range(1,n+1):
        if (i % 2) != 0:
            sum += i
    return sum

result = sumOdd4(n,sum)
print('Sum of odd number:',result)