# 3. Convert distant given in feet and inches into meter and centimeter.


feet   = float(input('Enter the feet for conversion: '))
inches = float(input('Enter the inches for conversion: '))


centimeters = (feet * 30.48) + (inches * 2.54)

meters = (feet * 0.3048) + (inches * 0.0254)


print('This is conversion of feet and inches into centimetes: ',centimeters,'cm')
print('This is conversion of feet and inches into meters: ',meters,'m')