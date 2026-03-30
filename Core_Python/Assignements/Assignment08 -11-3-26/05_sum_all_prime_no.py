# 5. Sum of all prime numbers between 1 to n




# without passing parameter
# wihtout return value
def sumEven1():
    n = int(input('Enter nmber:'))
    sum = 0
    
    for i in range(1,n+1):
        
        count = 0
        for j in range(1,i+1):
            if i % j == 0:
                count += 1
                
        if count == 2:
            sum += 1
    print('Sum of EVen numbers:',sum)
    
sumEven1()


# with passing parameter
# without return value
def sumEven2(n,sum):
    
    
    for i in range(1,n+1):
        
        count = 0
        for j in range(1,i+1):
            if i % j == 0:
                count += 1
                
        if count == 2:
            sum += 1
    print('Sum of even number:',sum)
    
n = int(input('Enter nmber:'))
sum = 0

sumEven2(n,sum)


# wihtout passing parameter
# with returning value
def sumEven3():
    n = int(input('Enter nmber:'))
    sum = 0
    
    for i in range(1,n+1):
        
        count = 0
        for j in range(1,i+1):
            if i % j == 0:
                count += 1
                
        if count == 2:
            sum += 1
    return sum

result = sumEven3()
print('Sum of even numbers:',result)


# with passing parameter
# with return value
def sum_prime(n):
    sum = 0
    
    for i in range(1,n+1):
        
        count = 0
        for j in range(1,i+1):
            if i % j == 0:
                count += 1
                
        if count == 2:
            sum += 1
    return sum
    
    
n = int(input('enter: '))
result = sum_prime(n)
print('Sum of even numbers:',result)