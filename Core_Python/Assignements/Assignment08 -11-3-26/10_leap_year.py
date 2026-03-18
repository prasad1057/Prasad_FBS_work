# 10. Write a program to check if entered year is a leap year or not.




# without passing parameter
# wihtout return value
def leap_year1():
    year = int(input('Enter the year: '))
    
    if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        print(f'{year} is leap year.')
    else:
        print(f'{year} is not leap year.')
    
leap_year1()



# with passing parameter
# without return value
def leap_year2(year):
    
    if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        print(f'{year} is leap year.')
    else:
        print(f'{year} is not leap year.')
        
year = int(input('Enter the year: '))
leap_year2(year)



# wihtout passing parameter
# with returning value
def leap_year3():
    
    year = int(input('Enter the year: '))
        
    return ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))

if leap_year3():
    print(f'{year} is leap year.')
else:
    print(f'{year} is not leap year.')
    
    

# with passing parameter
# with return value
def leap_year3(year):
        
    return ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))

year = int(input('Enter the year: '))

if leap_year3(year):
    print(f'{year} is leap year.')
else:
    print(f'{year} is not leap year.')
    