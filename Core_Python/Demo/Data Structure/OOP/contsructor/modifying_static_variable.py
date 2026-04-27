class Student:
                            # count means --> number of students
    count = 0               # when count will increase ? if the object will create then n only then count is increase
    
    def __init__(self, roll_no, name, age):
        
        Student.count += 1                  # here to access static variable we take class name with that variable name
        
        self.rn = roll_no
        self. name = name
        self.age = age
        
    def display(self):
        data = f'ROLL NO: {self.rn}\nNAME: {self.name}\nAGE:{self.age}'
        return data
    
    def totalCount():
        return Student.count                # here we retuning count with help of class name
    
    
s1 = Student(1, 'Prasad', 22)
s2 = Student(2, 'Karan', 21)
s3 = Student(1, 'Prasad', 22)
s4 = Student(2, 'Karan', 21)

print(s1.display())

print('-------------')

print('Total number of Students:',Student.totalCount())