# 10. Write a program to calculate area of an equilateral triangle.



import math

side = float(input("Enter the side of equilateral triangle: "))

area = (math.sqrt(3) / 4) * (side ** 2)

print("Area of Equilateral Triangle =", area)
