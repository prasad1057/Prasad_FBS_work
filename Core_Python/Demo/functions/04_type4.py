# with passing parameter
# with return value

def addition(num1,num2):
    
    sum = num1 + num2
    
    return sum

num1 = int(input('ENter the number1: '))
num2 = int(input('Enter the number2: '))

result = addition(num1,num2)
print('Addition',result)