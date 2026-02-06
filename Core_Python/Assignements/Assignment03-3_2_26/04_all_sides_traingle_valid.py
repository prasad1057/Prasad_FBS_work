# 4. Write a program to input all sides of a triangle and check whether triangle is valid or not.

side1 = int(input('Enter the side 1: '))
side2 = int(input('Enter the side 2: '))
side3 = int(input('Enter the side 3: '))

# all_side = side1 + side2 + side3

if side1 > 0 and side2 > 0 and side3 > 0:
    if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
        print('It is a traingel.')
    else:
        print('It is not traingle')
else:
    print('Triangle sides must be positive numbers.')

