
# 2. Write a program to calculate area of circle



# without passing parameter
# wihtout return value
def areaCircle1():
    pi = 3.14
    radius = int(input('Enter the radius: '))
    
    area = pi * radius**2
    print('Area of Circle is:',area)
    
areaCircle1()



# with passing parameter
# without return value
def areaCircle2(pi,radius):
    
    area = pi * radius**2
    print('Area of circle is:',area)
    
pi = 3.14
radius = int(input('Enter the radius: '))
areaCircle2(pi,radius)



# wihtout passing parameter
# with returning value
def areaCircle3():
    pi = 3.14
    radius = int(input('Enter the radius: '))
    
    area = pi * radius**2
    return area

result = areaCircle3()
print('Area of cirlce is:',result)



# with passing parameter
# with return value
def areaCircle4(pi,radius):
    
    area = pi * radius**2
    return area

pi = 3.14
radius = int(input('Enter the radius: '))

result = areaCircle4(pi,radius)
print('Area of circle is:',result)