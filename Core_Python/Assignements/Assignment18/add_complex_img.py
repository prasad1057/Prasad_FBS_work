'''
1. Create a class Complex Number with data members as real and imag and add following methods :
a. Constructor
b. Destructor
c. Overload +,- operator
'''


class Complex:
    
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    
    def __add__(self, other):                           #c1 + c2 --> self → represents c1   &   other → represents c2
        r = self.real + other.real                      
        i = self.img + other.img
        
        return Complex(r,i)                 # This line creates a new object. --> Constructor runs → 3rd time
    
    
    # display result
    def __str__(self):
        return f"{self.real} + {self.img}"
    
    
    def __del__(self):
        print('Destructor of Complex')
        
        
c1 = Complex(12,5j)                     #Constructor runs → 1st time
c2 = Complex(10,4j)                     #Constructor runs → 2nd time


print("Addition:", c1 + c2)                 #c1 + c2 --> self → represents c1   &   other → represents c2
