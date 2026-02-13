'''
2. Enter number of students from user. For those many students accept marks of 5
subject marks from user and calculate percentage. Display all percentage and
average percentage of students.
'''

n = int(input('Enter the number of students: '))

total_percentage = 0

for i in range(1,n+1):
    print(f'Student {i}: ')
    
    math = int(input('ENter the maths marks: '))
    phy = int(input('ENter the physics marks: '))
    chem = int(input('ENter the chemistry marks: '))
    bio = int(input('ENter the biology marks: '))
    history = int(input('ENter the history marks: '))
    
    total = math + phy + chem + bio + history
    
    percentage = (total / 500) * 100
    print(f'Percentage is: {percentage:.2f}')
    
    total_percentage += percentage
    

if n > 0:
    avg_percentage = total_percentage / n
    print(f'Average percentage of {n} students is:{avg_percentage} ')
else:
    print("No students entered.")

