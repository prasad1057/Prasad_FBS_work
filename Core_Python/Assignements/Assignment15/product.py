'''
2. Create a class Product with members as pid,pname,price and quantity .Add
following methods:
d. Constructor (Support both parameterized and parameterless)
e. Destructor
f. ShowBook
'''



class Product:
    
    def __init__(self, pid=None, pname=None, price=None, quantity=None):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        
    def showProduct(self):
        pid = self.pid if self.pid is not None else "Not Available"
        pname = self.pname if self.pname is not None else "No Data"
        price = self.price if self.price is not None else "0"
        quantity = self.quantity if self.quantity is not None else "Unknown"

        print("Product ID:", pid)
        print("PRODUCT NAME:", pname)
        print("PRICE:", price)
        print("QUANTITY:", quantity)
        

    def __del__(self):
        print('Product Destructor Method')
        
        
p1 = Product(1001, "TV", 70000, 1)
p1.showProduct()

print('--------------')

p2 = Product()
p2.showProduct()