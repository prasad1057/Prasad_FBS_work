class Vehicle:
    
    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price
        
    def display(self):
        return f'MODEL: {self.model}\nCOLOR: {self.color}\nPRICE: {self.price}\n'


class Car(Vehicle):
    def __init__(self, model, color, price, sunroof):
        super().__init__(model, color, price)
        self.sunroof = sunroof
        
    def display(self):
        data = super().display()
        data += f'SUNROOF: {self.sunroof}'
        return data
        #return super().display() + f'SUNROOF: {self.sunroof}'
        
c1 = Car('BMW', 'Black', 1000000, 'YES')

print(c1.display())


print('-------------------------------------------')


class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        
    def display(self):
        return f'NAME: {self.name}\nAGE: {self.age}\nCOLOR: {self.color}\n'
    

class Dog(Animal):
    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color)
        self.breed = breed
        
    def getData(self):
        data = super().display()
        data += f'BREED: {self.breed}'
        return data
        #return super().display() + f'BREED: {self.breed}'
        
        
d1 = Dog('Tuffy', '5 Years', 'White', 'Indian Spitz')
d2 = Dog('Jimmy', '7 Years', 'Brown', 'Labrador')



print(d1.getData())
print('-------------')
print(d2.getData())










