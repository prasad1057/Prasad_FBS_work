# 6. Write a Program to input two angles from user and find third angle of the triangle.

first_angle = int(input('ENter the first angle in degree %: '))
second_angle = int(input('ENter the second angle in degree %: '))

third_angle = 180 - (first_angle + second_angle)

print('A third angle of the traingle is: ',third_angle)