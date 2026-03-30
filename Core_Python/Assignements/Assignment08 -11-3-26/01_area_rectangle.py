# 1. Write a program to calculate area of rectangle




# without passing parameter
# wihtout return value
def areaRect1():
    length = float(input('Enter the length of rectangle: '))
    breadth = float(input('Enter the breadth of rectangle: '))
    
    area = length * breadth
    print('Area of rectangle:',area)
    
areaRect1()


# with passing parameter
# without return value
def areaRect2(length,breadth):
    
    area = length * breadth
    print('Area of rectangle:',area)
    
length = int(input('Enter the length of rectangle: '))
breadth = int(input('Enter the breadth of rectangle: '))

areaRect2(length,breadth)
    

# wihtout passing parameter
# with returning value
def areaRect3():
    
    length = float(input('Enter the length of rectangle: '))
    breadth = float(input('Enter the breadth of rectangle: '))
    
    area = length * breadth
    return area

result = areaRect3()
print('Area of rectangle:',result)


# with passing parameter
# with return value
def areaRect4(length,breadth):
    
    area = length * breadth
    return area

length = float(input('Enter the length of rectangle: '))
breadth = float(input('Enter the breadth of rectangle: '))

result = areaRect4(length,breadth)
print("Area of rectangle:",result)
    
