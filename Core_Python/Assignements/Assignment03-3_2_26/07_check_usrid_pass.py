# 7. Write a program to check if user has entered correct userid and password.

default_userid = 'Prasadk03'
default_pass = 'prasad0143'

user_input = input('Enter the user name: ')
user_pass  = input('Enter the user passwaard: ')

if user_input == default_userid and user_pass == default_pass:
    print("Login Successful")
else:
    print("Invalid UserID or Password")
