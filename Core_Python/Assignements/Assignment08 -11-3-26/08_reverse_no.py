# 8. Write a program find reverse of a number




# without passing parameter
# wihtout return value
def reverse_no1():
    n = int(input('Enter the number: '))
    rev_no = 0
    
    while (n > 0):
        digit = n % 10
        rev_no = rev_no * 10 + digit
        n = n // 10
    print('Reverse No:',rev_no)
    
reverse_no1()
    


# with passing parameter
# without return value
def reverse_no2(n,rev_no):
    
    while (n > 0):
        digit = n % 10
        rev_no = rev_no * 10 + digit
        n = n // 10
    print('Reverse No:',rev_no)
    
n = int(input('Enter the number: '))
rev_no = 0

reverse_no2(n,rev_no)



# wihtout passing parameter
# with returning value
def reverse_no3():
    n = int(input('Enter the number: '))
    rev_no = 0
    
    while (n > 0):
        digit = n % 10
        rev_no = rev_no * 10 + digit
        n = n // 10
    return rev_no

result = reverse_no3()
print('Reverse No:',result)




# with passing parameter
# with return value
def reverse_no4(n):

    rev_no = 0
    while (n > 0):
        digit = n % 10
        rev_no = rev_no * 10 + digit
        n = n // 10
    return rev_no

n = int(input('Enter the number: '))


result = reverse_no4(n)
print('Reverse No:',result)