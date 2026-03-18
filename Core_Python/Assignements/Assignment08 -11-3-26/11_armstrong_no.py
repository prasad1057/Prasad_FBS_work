# 11. WAP to check if a given number is Armstrong number or not. For each task create separate functions.


# without passing parameter
# wihtout return value
def armstrong1():
    n = int(input('Enter the number: '))
    og_no = n
    
    # 1. to store count of number
    temp = n
    count = 0    
    while (temp > 0):
        count += 1
        temp = temp // 10
    
    # 2. calculate sum
    temp = n
    sum = 0
    while (temp > 0):
        digit = temp % 10
        sum += digit ** count
        temp = temp // 10
    
    if og_no == sum:
        print(f'{og_no} is armstrong number')
    else:
        print(f'{og_no} is not armstrong number')
        
armstrong1()
    


# with passing parameter
# without return value
def armstrong2(n):
    og_no = n
    
    temp = n
    count = 0
    while(temp > 0):
        count += 1
        temp = temp // 10
        
    temp = n
    sum = 0
    while (temp > 0):
        digit = temp % 10
        sum += digit ** count
        temp = temp // 10
        
    if og_no == sum:
        print(f'{og_no} is armstrong number')
    else:
        print(f'{og_no} is not armstrong number')
     
n = int(input('Enter the number: '))   
armstrong2(n)




# wihtout passing parameter
# with returning value
def armstrong3():
    
    n = int(input('Enter the number: '))
    og_no = n
    
    temp = n
    count = 0
    while (temp > 0):
        count += 1
        temp = temp // 10
    
    temp = n
    sum = 0
    while(temp > 0):
        digit = temp % 10
        sum += digit ** count
        temp = temp // 10
        
    return og_no, (og_no == sum)

num, result = armstrong3()

if result:
    print(f'{num} is armstrong number')
else:
    print(f'{num} is not a armstrong number')


# with passing parameter
# with return value
def armstrong3(n):
    
    og_no = n
    
    temp = n
    count = 0
    while (temp > 0):
        count += 1
        temp = temp // 10
    
    temp = n
    sum = 0
    while(temp > 0):
        digit = temp % 10
        sum += digit ** count
        temp = temp // 10
        
    return og_no, (og_no == sum)

n = int(input('Enter the number: '))

num, result = armstrong3(n)

if result:
    print(f'{num} is armstrong number')
else:
    print(f'{num} is not a armstrong number')