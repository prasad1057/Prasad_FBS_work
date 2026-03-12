# without passing parameter
# with returning value

def addition():
    
    num1 = int(input('ENter the number1: '))
    num2 = int(input('Enter the number2: '))
    
    sum = num1 + num2
    
    return sum

result = addition()
print('Addition',result)