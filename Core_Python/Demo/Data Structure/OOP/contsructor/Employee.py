# Without Constructor

'''
class Employee:
    
    def setData(self, emp_id, emp_name, dept_name):
        self.id = emp_id
        self.ename = emp_name
        self.dname = dept_name
        
    def getData(self):
        print('Employee ID:',self.id)
        print('Employee Name:',self.ename)
        print('Employee Department:',self.dname)
        
        
obj1 = Employee()
obj1.setData(101, 'PrasadK', 'IT')


obj2 = Employee()
obj2.setData(102, 'KaranK', 'DS')

obj1.getData()
print('------------------')
obj2.getData()

'''

# WIth Constructor

class Employee:
    
    def __init__(self, emp_id, emp_name, dept_name):
        
        self.id = emp_id
        self.ename = emp_name
        self.dname = dept_name
        
        
    def getData(self):
        print('Employee ID:',self.id)
        print('Employee Name:',self.ename)
        print('Employee Department:',self.dname)
        
        
e1 = Employee(101, 'PrasadK', 'IT')
e1.getData()