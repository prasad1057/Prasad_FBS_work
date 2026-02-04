# 1. Write a program to calculate the percentage of student based on marks of any 5 subjects.

physics     = int(input('Enter physics masrks: '))
chemistry   = int(input('Enter chemistry masrks: '))
maths       = int(input('Enter maths masrks: '))
biology     = int(input('Enter biology masrks: '))
history     = int(input('Enter history masrks: '))

percenatge = (physics + chemistry + maths + biology + history) / 5

print('Percentage of student based on marks of any 5 subjects is: ',percenatge)
