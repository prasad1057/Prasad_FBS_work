# 9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)

math = int(input('ENter the maths marks: '))
phy = int(input('ENter the physics marks: '))
chem = int(input('ENter the chemistry marks: '))
bio = int(input('ENter the biology marks: '))
history = int(input('ENter the history marks: '))

marks = math + phy + chem + bio + history
percentage = (marks / 500) * 100

print("Total Marks:", marks)
print("Percentage:", percentage)

if percentage >= 80:
    print("First Class")

elif percentage >= 60:
    print("Second Class")

elif percentage >= 35:
    print("Third Class")

else:
    print("You Failed")