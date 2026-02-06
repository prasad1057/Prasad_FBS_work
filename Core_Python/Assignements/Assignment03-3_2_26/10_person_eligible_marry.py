# 10. Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

gender = input('ENter gender (M/F): ')
age = int(input('ENter the age: '))

if gender in ['F','f','Female','FEMALE','female']:
    if age >= 18:
        print('Eligible for marriage.')
    else:
        print('Pehele padhai kar le.')
else:
    if age >= 21:
        print('Eligible for marriage.')
    else:
        print('Bada to ho ja.')
        
        
'''
gender = input("Enter gender (M/F): ").lower()
age = int(input("Enter the age: "))

if gender == 'f' or gender == 'female':
    if age >= 18:
        print("Eligible for marriage.")
    else:
        print("Not eligible for marriage.")

elif gender == 'm' or gender == 'male':
    if age >= 21:
        print("Eligible for marriage.")
    else:
        print("Not eligible for marriage.")

else:
    print("Invalid gender entered.")

'''
        