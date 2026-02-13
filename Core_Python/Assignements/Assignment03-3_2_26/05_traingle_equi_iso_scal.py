# 5. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

# equilateral --> means all sides are equal
# isosceles   --> means any two sides are equal
# scalene     --> means all sides are different

side1 = int(input('Enter the side 1: '))
side2 = int(input('Enter the side 2: '))
side3 = int(input('Enter the side 3: '))

if (side1 > 0 and side2 > 0 and side3 > 0):
    
    if (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2):        # TO check TRaingle Validity
        
        if side1 == side2 and side2 == side3:
            print('It is an Equilateral Traingle.')
        elif (side1 == side2 or side1 == side3 or side2 == side3):
            print('It is an Isoscles Traingle')
        else:
            print('Is is an Scalene Traingle')
            
    else:
        print('Not a valid triangle.')
        
else:
    print('Triangle sides must be positive numbers.')