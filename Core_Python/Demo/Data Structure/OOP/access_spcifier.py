class Employee:
    def __init__(self, id, name, sal):
        self.id = id                        #public
        self._name = name                   #protected
        self.__sal = sal                    #private
        

e1 = Employee(101, 'Prasad', 20000)

print(e1.id)
print(e1._name)

#print(e1.__sal)             # we can not access private easily
print(e1._Employee__sal)            # naming convention to access private