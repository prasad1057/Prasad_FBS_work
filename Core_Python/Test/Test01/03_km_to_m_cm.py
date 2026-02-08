# 3. Write a program to accept distance in km and convert it into meters and centimeters both.

'''
1 km -> 1000 m
1 m  -> km * 1000

1 m  -> 100 cm
1 cm  -> m * 100
1 cm  -> km * 100000
'''

kilo_meter = int(input('Enter the kilometer: '))

meter = kilo_meter * 1000               
centimeter = kilo_meter * 100000

print('Meter is: ',meter)
print('Centimter is: ',centimeter)