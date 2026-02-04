# 11. Find the area and circumference of circle.

import math

radius = float(input("Enter radius of circle: "))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print("Area of Circle:", area)
print("Circumference of Circle:", circumference)
