# 3. Write a program to input angles of a triangle and check whether triangle is valid or not. 

first_angle = int(input('Emter the first angle of traingle: '))
second_angle = int(input('Emter the Second angle of traingle: '))
third_angle = int(input('Emter the Third angle of traingle: '))

all_angles = first_angle + second_angle + third_angle

if first_angle> 0 and second_angle > 0 and third_angle > 0 and all_angles == 180:
    print("Triangle is Valid.")
else:
    print("Triangle is Not Valid.")