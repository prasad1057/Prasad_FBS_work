'''
1. Create a class Student with following
a. data members :
i. StudentId
ii. Name
iii. Age
iv. Percentage
b. Add the following methods :
i. Parameterized constructor
ii. Display
iii. Accept
iv. Method CalculateRank
v. Override __str__ Method

'''


class Student:
    
    # Parameterized constructor
    def __init__(self, stdId, name, age, percentage):
        self.stdId = stdId
        self.name = name
        self.age = age
        self.percentage = percentage
        
        
    # Accept method
    def Accept(self):
        self.stdId = int(input("Enter your ID: "))
        self.name = input("Enter your Name: ")
        self.age = int(input("Enter your AGE: "))
        self.percentage = int(input("Enter your Percentage: "))
        
        
    # Display method
    def display(self):
        print("STUDENT ID:", self.stdId)
        print("NAME:", self.name)
        print("AGE:", self.age)
        print("PERCENTAGE:", self.percentage)
        
        
    # Calculate Rank
    def CalculateRank(self):
        
        if self.percentage >= 90:
            print("First Rank")
            
        elif self.percentage >= 75:
            print("Second Rank")
            
        elif self.percentage >= 60:
            print("Third Rank")
            
        else:
            print("Fail")
            
            
    # Override __str__
    def __str__(self):
        return f"Student INFO({self.stdId}, {self.name}, {self.age}, {self.percentage})"


# s1 = Student(101, "Prasad", 21, 85)             # Parameterized constructor

# s1.Accept()                         # user input

# print('--------------')

# s1.display()                      # if u want to display the parameter constructor then call display method direcylt and if u want to display the user input as output then call accept() method first then display() method
# s1.CalculateRank()

# print(s1)



