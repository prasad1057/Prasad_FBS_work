'''
3. Create a class Shirt with members as sid,sname,type(formal etc), price and
size(small,large etc) .Add following methods:
g. Constructor (Support both parameterized and parameterless)
h. Destructor
i. ShowBook
'''


class Shirt:
    
    def __init__(self, sid=None, sname=None, type=None, price=None, size=None):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size
        
    def showShirt(self):
        sid = self.sid  if self.sid is not None else "Not Availabel"
        sname = self.sname if self.sname is not None else "Unknown name"
        type = self.type if self.type is not None else "No matching"
        price = self.price if self.price is not None else "Unknown"
        size = self.size if self.size is not None else "Unknown"

        print("Shirt ID:",sid)
        print("Shirt Name:",sname)
        print("SHIRT TYPE:",type)
        print("PRICE:",price) 
        print("SIZE:",size) 
        
    def __del__(self):
        print('Shirt Destructor Method')
        
        
s1 = Shirt(101, "COttonking", "Formal", 2000, "Large")    
s2 = Shirt(102, "CamBridge", "Casual", 1500, "Medium")

s1.showShirt()
print('---------')
s2.showShirt()

print('--------------------------')

s3 = Shirt()
s3.showShirt()    