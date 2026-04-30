from abc import ABC,abstractclassmethod

class Employee:
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal
        
    @abstractclassmethod
    def calSal(self):
        print('EMployee abstarct method')
        pass
        
        
class Teacher(Employee):
    def __init__(self, id, name, sal, incentive):
        super().__init__(id, name, sal)
        self.incentive = incentive
        
    def calSal(self):
        print(f'Total Salary: {self.sal + self.incentive}')
        
        
e1 = Teacher(11, 'Prasad Sir', 1000, 150)
e1.calSal()

