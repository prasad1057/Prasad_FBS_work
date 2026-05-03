def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    if num1 > num2:
        return num1 - num2
    else:
        return num2 - num1

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

'''
# DOnt Use this:

# def main():
#     print(addition(10,20))

# if __name__ == '__main__':
#     main()
'''


if __name__ == '__main__':
    print(addition(4,5))

