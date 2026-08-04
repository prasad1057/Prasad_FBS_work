'''
Encapsulation is the process of hiding data and providing controlled access through methods. 
In my code, __brand and __model are private variables, and getBrand() and getModel() are public
methods used to access them. Since the data cannot be accessed directly, this class demonstrates 
encapsulation.
'''

class Car:

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def getBrand(self):
        return self.__brand

    def getModel(self):
        return self.__model


    #Display full details
    def fullDetails(self):
        return f'Brand: {self.__brand}, Model: {self.__model}'


c1 = Car('Tesla', 'Model S')

# Access using methods
print(c1.getBrand())
print(c1.getModel())
print(c1.fullDetails())

# Direct access (will give an error)
# print(c1.__brand)
# print(c1.brand)