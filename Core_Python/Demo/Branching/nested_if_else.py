gender = input('ENter gender (M/F): ')
age = int(input('ENter the age: '))

if gender in ['F','f','Female','FEMALE','female']:
    if age > 18:
        print('Eligible for marriage.')
    else:
        print('Pehele padhai kar le.')
else:
    if age > 20:
        print('Eligible for marriage.')
    else:
        print('Bada to ho ja.')
        
        
# Q. Check person is eligibel for voting or not
age = int(input('ENter age for voting: '))

if age > 0:
    if age > 17 and age < 100:
        print('Eligible for voting.')
    else:
        print('Not eligible.')
else:
    print('Phele age to dekh')