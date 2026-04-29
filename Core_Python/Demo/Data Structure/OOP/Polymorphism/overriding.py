class Vehicle:
    
    def brake(self):
        return 'Vehicle Stopped..'
        
        
class Car(Vehicle):
    
    def brake(self):
        return 'Car Stopped..'
        
        
c1 = Car()
print(c1.brake())