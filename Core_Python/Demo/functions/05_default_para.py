# why --> To make paramter optional
# what --> Assigning value to parameter in function defination
# how --> If we pass value to default para, it takes passed value, if we dont then it takes default value

def add(num1, num2, num3=0, num4=1):
    print('Addition',num1 + num2 + num3 + num4)
    
add(10,20)


# Q. WAP to take states of employee
def employee(id, name, salary=0, dept='Not Assigned'):
    print('Emp ID:',id)
    print('Emp Name:',name)
    print('Emp Salary:',salary)
    print('Emp department:',dept)

employee(101,'prasad')
