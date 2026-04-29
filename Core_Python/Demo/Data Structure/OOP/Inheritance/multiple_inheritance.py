'''
class Singer:
    def __init__(self, song_type):
        self.song_type = song_type
        
    def display(self):
        print('Display Method of Singer')


class Dancer:
    def __init__(self, dance_type):
        self.dance_type = dance_type
        
    def display(self):
        print('Display Method of Dancer')
        

class Performer(Singer, Dancer):                        # here if we pass Singer as first parameter then the Performer gets display method from Singer class.
    def __init__(self, song_type, dance_type, exp):
        
        Singer.__init__(self,song_type)
        Dancer.__init__(self, dance_type)
        self.exp = exp
        
    def show(self):
        print('Display method of Performer')
        
    
p1 = Performer('Classical', 'Katthak', 4)
p1.display()                    

'''



class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        
    def show(self):
        return f"NAME: {self.name}\nAGE: {self.age}\nEMAIL: {self.email}\n"
    
    
class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary
        
    def get(self):
        return f"EMP-ID: {self.emp_id}\nSALARY: {self.salary}\n"
    
    
class HR(Employee, Person):
    def __init__(self, name, age, email, emp_id, salary, hr_id):
        
        # Call Person constructor
        Person.__init__(self, name, age, email)
        
        # Call Employee constructor
        Employee.__init__(self, emp_id, salary)
        
        # HR specific attribute
        self.hr_id = hr_id
        
    def present(self):
        data = Person.show(self)
        data += Employee.get(self)
        data += f"HR-ID: {self.hr_id}"
        return data
    
    
hr1 = HR("Prasad", 21, "prasad@gmail.com", "emp123", 1000, "hr100")

print(hr1.present())