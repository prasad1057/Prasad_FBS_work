'''
8. Write a program to prompt user to enter userid and password. After verifying
userid and password display a 4 digit random number and ask user to enter the
same. If user enters the same number then show him success message otherwise
failed. (Something like captcha)
'''



default_userid = 'Prasadk03'
default_pass = 'prasad0143'
captcha = 'abcd'


user_input = input('Enter the user name: ')
user_pass  = input('Enter the user passwaard: ')

if user_input == default_userid and user_pass == default_pass:
    user_captcha = input('ENter the captcha: ')
    if captcha == user_captcha:
        print('Login Successful')
    else:
        print('Enter captcha is invalid')
else:
    print("Invalid UserID or Password")


# USING random module

'''
import random

default_userid = "Prasadk03"
default_pass = "prasad0143"

user_input = input("Enter the user name: ")
user_pass = input("Enter the user password: ")

if user_input == default_userid and user_pass == default_pass:
    
    captcha = random.randint(1000, 9999)         # Generate a random whole number between 1000 and 9999 (both included)
    print("Captcha:", captcha)
    
    user_captcha = int(input("Enter the captcha: "))
    
    if captcha == user_captcha:
        print("Login Successful")
    else:
        print("Entered captcha is invalid")

else:
    print("Invalid UserID or Password")

'''