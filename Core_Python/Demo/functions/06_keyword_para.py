# why --> TO neglect position paramter concept
# what --> Assignung value to parameters in function
# how --> Nmae of parameter in fucntion call & fucntion definition should be same

def employee(id, name, salary, dept):
    print('Emp ID:',id)
    print('Emp Name:',name)
    print('Emp Salary:',salary)
    print('Emp department:',dept)

employee(101,'prasad','10000','Tester')

print('###############')

employee(name='prasad',salary='10000',dept='Tester',id=591)