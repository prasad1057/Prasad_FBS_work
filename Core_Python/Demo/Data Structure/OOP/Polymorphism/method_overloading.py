def add(num1, num2):
    return num1 + num2


#solution --> default parameter

def add(num1, num2, num3=0):
    return num1 + num2 + num3


print(add (10,20))
print(add(10,20,30))