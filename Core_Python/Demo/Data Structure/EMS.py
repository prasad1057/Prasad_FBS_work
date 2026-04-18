def addEmp(id, name, sal, dept):
    
    if (id not in emp_details.keys()):
        emp_details[id] = [id, name, sal, dept]
        return 'Employee Added Successfully.'
    else:
        return f'{id} already exist'
        

def updEmp(id):
    if (id in emp_details):
        
        emp = emp_details[id]
        
        print('Note: If dont want to change the field leave blank.')
        name = input(f'Enter new Name:({emp[1]}): ') or emp[1]
        sal = input(f'Enter new SALARY:({emp[2]}): ') or emp[2]
        dept = input(f'Enter new DEPARTMENT:({emp[3]}): ') or emp[3]
        
        emp_details[id] = [id, name, sal, dept]
        return 'Employee Updated Successfully'
        
    else:
        return f'{id} not exist'



emp_details = {}

ch = 0

while (ch != '6'):
    print('''Please Select Option
          1. Add Employee
          2. Show all Employees
          3. Update Employess
          4. Delete Employees
          5. Search Employees
          6. Exit
          ''')
    
    ch = input('Enter choice: ')
    
    if (ch == '1'):
        id = input('Enter ID: ')
        name = input('Enter NAME: ')
        sal = float(input('Enter SALARY: '))
        dept = input('Enter DEPARTMENT: ')
        
        res = addEmp(id, name, sal, dept)
        print(res)

    elif (ch == '2'):
        print(emp_details)
    
    elif (ch == '3'):
        id = input('Enter ID: ')
        res = updEmp(id)
        print(res)
    
    elif (ch == '4'):
        pass
    
    elif (ch == '5'):
        pass
    
    elif (ch == '6'):
        print('Mandal Abhari ahee !!!!!')
        
    else:
        print('Invalid Input')