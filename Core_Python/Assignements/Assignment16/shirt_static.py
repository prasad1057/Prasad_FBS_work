'''
3. Create a class Shirt with members as sid,sname,type(formal etc), price and
size(small,large etc) .Add following methods:
j. Constructor (Support both parameterized and parameterless)
k. Destructor
l. ShowBook
m. For each size of shirt price should change by 10%.
(eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
xlarge=1300) Use static concept.
'''


class Shirt:
    
    discount = 10
    
    def __init__(self, sid=None, sname=None, type=None, price=None, size=None):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size
        
    def showShirt(self):
        print("SHIRT ID:",self.sid)
        print("SHIRT NAME:",self.sname)
        print("PRICE:",self.price)
        print("SIZE:",self.size)
        
    def applyDisShirt(self):
        if self.size == "small":
            new_price = self.price
        
        elif self.size == "medium":
            new_price = self.price + (self.price * Shirt.discount / 100)
            
        elif self.size == "large":
            new_price = self.price + (self.price * 2 * Shirt.discount / 100)

        elif self.size == "xlarge":
            new_price = self.price + (self.price * 3 * Shirt.discount / 100)
            
        else:
            new_price = self.price
            
        return new_price
            
            
    def __del__(self):
        print('Shirt Destructor Method')
        
        

s1 = Shirt(101, "Arrow", "Formal", 1000, "small")
s2 = Shirt(101, "CottonKing", "Casual", 1500, "medium")
s3 = Shirt(101, "CamBridge", "Formal", 800, "large")
s4 = Shirt(101, "Arrow", "Formal", 1000, "xlarge")
s5 = Shirt(101, "H&M", "Casual", 2000, "xlarge")


s1.showShirt()

print("Price After Size change(s1):",s1.applyDisShirt())
print("Price After Size change(s1):",s2.applyDisShirt())
print("Price After Size change(s3):",s3.applyDisShirt())
print("Price After Size change(s4):",s4.applyDisShirt())
print("Price After Size change(s4):",s5.applyDisShirt())
            
          
        

    