'''
3. Create a class MedicalStudent inherited from Student with following :

i. Data members :Specialization
ii. MarksOfInternship
b. Add the following methods :
i. Parameterized constructor
ii. Display
iii. Accept
iv. override Method CalculateRank
v. Override __str__ Method
'''

from student import Student

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
        
    
#     def Accept(self):
#         self.stdId = int(input('Enter Student Id: '))
#         self.name = input('ENter STudent Name: ')
#         self.age = int(input('ENter AGe: '))
#         self.percentage = int(input('Enter Percentage: '))
        
        
#     def CalRank(self):
        
#         if self.percentage >= 80:
#             print("General Rank A")
            
#         elif self.percentage >= 60:
#             print("General Rank B")
            
#         else:
#             print("General Rank C")
            
            
            
#     def __str__(self):
#         return f'STudent Info: {self.stdId}, {self.name}, {self.age}, {self.percentage}'
    
    

class MedStudent(Student):
    def __init__(self, stdId, name, age, percentage, spcialization, marksOfInternship):
        super().__init__(stdId, name, age, percentage)
        self.spcialization = spcialization
        self.marksOfInternship = marksOfInternship
        
    
    def display(self):
        super().display()
        print('Speialization:',self.spcialization)
        print('Marks Of Internship:',self.marksOfInternship)
    
    
    def Accept(self):
        self.stdId = int(input('Enter Student Id: '))
        self.name = input('ENter STudent Name: ')
        self.age = int(input('ENter AGe: '))
        self.percentage = int(input('Enter Percentage: '))
        self.spcialization = input('Specialization: ')
        self.marksOfInternship = int(input('Enter the Marks of Internship: '))
        
    
    def CalRank(self):

        if self.percentage >= 90:
            print("Excellent Medical Rank")

        elif self.percentage >= 75:
            print("Very Good Medical Rank")

        elif self.percentage >= 60:
            print("Good Medical Rank")

        else:
            print("Needs Improvement")
        
        
    
    
    def __str__(self):
        return super().__str__() + f"{self.spcialization}, {self.marksOfInternship}"
    
    
    
m1 = MedStudent(101, 'Prasad', 21, 89, 'Nursing', 500)
m1.Accept()
print('---------------')
m1.display()