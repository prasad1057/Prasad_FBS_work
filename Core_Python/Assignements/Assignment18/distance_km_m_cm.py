'''
2. Create a class Distance with data members as km,m and cm and add following methods :
a. Constructor
b. Destructor
c. Overload +,- operator
'''


class Distance:
    def __init__(self, km, m, cm):
        self.kilometer = km
        self.meter = m
        self.centimeter = cm
        
        
    def __add__(self, other):
        k = self.kilometer + other.kilometer
        m = self.meter + other.meter
        c = self.centimeter + other.centimeter
        
        return Distance(k,m,c)
    
    
    def __sub__(self, other):
        k = self.kilometer - other.kilometer
        m = self.meter - other.meter
        c = self.centimeter - other.centimeter
        
        return Distance(k, m, c)
    
    
    def __str__(self):
        return f"{self.kilometer} km {self.meter} m {self.centimeter} cm"
    
    def __del__(self):
        print("Destructor method of Distance")
        

d1 = Distance(10,30,100)
d2 = Distance(20,50,150)

print("Addition:", d1 + d2)
print("Subtraction:", d1 - d2)