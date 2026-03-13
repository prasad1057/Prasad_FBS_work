
# b. 1!+ 2! + 3! + 4!+..... + n!




# without passing parameter
# wihtout return value
def factSeries1():
    
    n = int(input('Enter nmber:'))
    fact = 1
    
    for i in range(1,n+1):
        fact *= i      
    print('Factorial:',fact)

factSeries1()


# with passing parameter
# without return value
def factSeries2(n,fact):
    
    for i in range(1,n+1):
        fact *= i
    print('Factorial:',fact)
    
n = int(input('Enter nmber:'))
fact = 1

factSeries2(n,fact)


# wihtout passing parameter
# with returning value
def factSeries3():
    
    n = int(input('Enter nmber:'))
    fact = 1
    
    for i in range(1,n+1):
        fact *= i
    return fact

result = factSeries3()
print('Factorial:',result)      #print(factSeries3())


# with passing parameter
# with return value
def factSeries4(n,fact):
    
    for i in range(1,n+1):
        fact *= i
    return fact

n = int(input('Enter nmber:'))
fact = 1

result = factSeries4(n,fact)
print('Factorial:',result)