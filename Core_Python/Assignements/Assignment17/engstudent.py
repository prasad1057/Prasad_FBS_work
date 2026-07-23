'''
2. Create a derived class from Student as EnggStudent with :
a. Data members as :
i. Branch
ii. InternalMarks
b. Add the following methods :
i. Parameterized constructor
ii. Display
iii. Accept
iv. override Method CalculateRank
v. Override __str__ Method
'''



# class Student:
#     def __init__(self, stdId, name, age, percentage):
#         self.stdId = stdId
#         self.name = name
#         self.age = age
#         self.percentage = percentage
        
        
        
#     def display(self):
#         print("STUDENT ID:", self.stdId)
#         print("NAME:", self.name)
#         print("AGE:", self.age)
#         print("PERCENTAGE:", self.percentage)
        
        
#     def CalculateRank(self):
        
#         if self.percentage >= 80:
#             print("General Rank A")
            
#         elif self.percentage >= 60:
#             print("General Rank B")
            
#         else:
#             print("General Rank C")
            
            
            
#     def __str__(self):
#         return f"Student INFO({self.stdId}, {self.name}, {self.age}, {self.percentage})"
    
    
from student import Student

    
class EnggStudent(Student):
    def __init__(self, stdId, name, age, percentage, branch, internalMarks):
        super().__init__(stdId, name, age, percentage)
        self.branch = branch
        self.internalMarks = internalMarks
        
        
    def Accept(self):
        self.stdId = int(input('Enter the STudent ID: '))
        self.name = input('ENter the Name: ')
        self.age = int(input('ENter the AGe:'))
        self.percentage = int(input('Enter the Percentage: '))
        self.branch = input('ENter the Branch: ')
        self.internalMarks = int(input('Enter the Internal Marks: '))
        
        
    def display(self):
        super().display()
        print("BRANCH:", self.branch)
        print("INTERNAL MARKS:", self.internalMarks)
        
        
    def CalculateRank(self):
        
        if self.percentage >= 90:
            print("First Rank")
            
        elif self.percentage >= 75:
            print("Second Rank")
            
        elif self.percentage >= 60:
            print("Third Rank")
            
        else:
            print("Fail")
    
    
    def __str__(self):
        return f"Student INFO({self.stdId}, {self.name}, {self.age}, {self.percentage}, {self.branch}, {self.internalMarks})"
    
    

e1 = EnggStudent(101, 'Prasad', 21, 85, 'IT', 20)

e1.Accept()
print('------------')
e1. display()



print('############## Super CLass Information ##############')

s1 = Student(102, 'karan', 12, 56)

s1.display()

s1.CalculateRank()   # calls parent method
