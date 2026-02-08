'''
1. Write a program to find the area and perimeter of following
figure (Accept the length, breadth and radius from user: 
(Note: The figure shown is a rectangle with a semicircle attached to the right side.)
'''

'''
1️⃣ Area
Total Area =
Area of Rectangle + Area of Semi-circle
Area of rectangle = L × B
Area of semi-circle = (π × R²) / 2

2️⃣ Perimeter

Perimeter means outer boundary only.
In this figure, perimeter includes:
Left vertical side of rectangle
Top horizontal side
Bottom horizontal side
Curved part of semi-circle

It does NOT include the straight side between rectangle and semicircle.

So perimeter consists of:
Rectangle top = L
Rectangle bottom = L
Rectangle left side = B
Semi-circle curved length = π × R
'''

length = int(input('Enter the length: '))
breadth = int(input('ENter the breadth: '))
radius = float(input('Enter the radius: '))

pi = 3.14

area_reactnagle = length * breadth
area_half_circle = pi * (radius ** 2) / 2

total_area = area_reactnagle + area_half_circle
print('Total area is: ',total_area)



total_perimeter = (2 * length) + breadth + (pi * radius) 
print('TOtal perimter is: ',total_perimeter)