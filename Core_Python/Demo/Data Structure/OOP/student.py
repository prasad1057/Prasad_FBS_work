class Student:
    
    def setData(self, roll_no, name, age):

        self.rn = roll_no
        self.nm = name
        self.age = age
        
        
    def getData(self):
        print('ROLL NO:',self.rn)
        print('NAME:',self.nm)
        print('AGE',self.age)
        
        
obj1 = Student()
obj1.setData(1,'Prasad', 22)

obj2 = Student()
obj2.setData(2,'Karan', 23)


obj1.getData()
print('######################')
obj2.getData()