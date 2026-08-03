# 7. Write a program to find sum of digits of a number.




# without passing parameter
# wihtout return value
def sum_digit1():
    n = int(input("Enter number: "))
    
    total = 0
    
    while n > 0:
        digit = n % 10
        total = digit + total
        n = n // 10
        
    print('Sum of digit:',total)
        
sum_digit1()



# with passing parameter
# without return value
def sum_digit2(n,total):
    
    while n > 0:
        digit = n % 10
        total = digit + total
        n = n // 10
        
    print('Sum of digit:',total)

n = int(input("Enter number: "))
total = 0
sum_digit2(n,total)



# wihtout passing parameter
# with returning value
def sum_digit3():
    n = int(input("Enter number: "))
    total = 0
    
    while(n > 0):
        digit = n % 10
        total = digit + total
        n = n // 10
    return total


result = sum_digit3()
print('Sum of digit:',result)



# with passing parameter
# with return value
def sum_digit4(n):

    total = 0
    while(n > 0):
        digit = n % 10
        total = digit + total
        n = n // 10
    return total

n = int(input("Enter number: "))

result = sum_digit4(n)
print('Sum of digit:',result)