# 9. Write a program to check if entered number is a palindrome or not.



# without passing parameter
# wihtout return value

# with passing parameter
# without return value

# wihtout passing parameter
# with returning value

# with passing parameter
# with return value




# without passing parameter
# wihtout return value
def pallindrome1():
    n = int(input('Enter the number: '))
    og_no = n
    rev_no = 0
    
    while (n > 0):
        digit = n % 10
        rev_no = rev_no * 10 + digit
        n = n // 10
        
    if (og_no == rev_no):
        print('Its a Pallindrome')
    else:
        print('Its not Pallindrome')

pallindrome1()



# with passing parameter
# without return value
def pallidrome2(n):
    rev_no = 0
    og_no = n

    while (n > 0):
        digit = n % 10
        rev_no = rev_no * 10 + digit
        n = n // 10
        
    if (og_no == rev_no):
        print('Its a Pallindrome')
    else:
        print('Its not a Pallindrome')

n = int(input('Enter the number: '))

pallidrome2(n)




# wihtout passing parameter
# with returning value
def pallindrome3():
    n = int(input('Enter the number: '))
    rev_no = 0
    og_no = n
    
    while (n > 0):
        digit = n % 10
        rev_no = rev_no * 10 + digit
        n = n // 10
    return og_no == rev_no
        
if pallindrome3():
    print('Its a Pallindrome')
else:
    print('Its not a Pallindrome')
    
    

# with passing parameter
# with return value
def pallindrome4(n):
    og_no = n
    rev_no = 0
    
    while (n > 0):
        digit = n % 10
        rev_no = rev_no * 10 + digit
        n = n // 10
        
    return og_no == rev_no

n = int(input('Enter the number: '))
if pallindrome4(n):
    print('Its a Pallindrome')
else:
    print('Its not a Palldindrome')