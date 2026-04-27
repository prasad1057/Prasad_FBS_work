# Parameter Constructor


class Student:
    
    def __init__(self,  roll_no, name, age):

        self.rn = roll_no
        self.nm = name
        self.age = age
        
    def getData(self):
        print('ROLL NO:',self.rn)
        print('NAME:',self.nm)
        print('AGE',self.age)
        

s1 = Student(1,'Prasad', 22)
s1.getData()



print('-----------------------')

# Default Constructor


class Student:
    
    def __init__(self,  roll_no=101, name='', age=0):

        self.rn = roll_no
        self.nm = name
        self.age = age
        
    def getData(self):
        print('ROLL NO:',self.rn)
        print('NAME:',self.nm)
        print('AGE',self.age)
        

s1 = Student()
s1.getData()