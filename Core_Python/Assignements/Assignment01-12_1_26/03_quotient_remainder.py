# 3. Program to find quotient and remainder of two numbers.

number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))

if number2 == 0:
    print("Division not possible (number2 is zero)")
else:
    quotient = number1 // number2
    remainder = number1 % number2
    
    print("Quotient =", quotient)
    print("Remainder =", remainder)


