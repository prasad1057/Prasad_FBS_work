'''
2. Create a class Product with members as pid,pname,price and quantity .Add
following methods:
e. Constructor (Support both parameterized and parameterless)
f. Destructor
g. ShowBook
h. Add static member discount.
i. Provide methods for applying discount on price of product.
'''


class Product:
    
    discount = 10
    
    def __init__(self, pid=None, pname=None, price=None, quantity=None):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        
    def showProduct(self):
        
        print("Product ID:",self.pid)
        print("PRODUCT NAME:", self.pname)
        print("PRICE:", self.price)
        print("QUANTITY:", self.quantity)
        
        
    # method to apply discount
    def applyDiscount(self):
        new_price = self.price - (self.price * Product.discount / 100)
        return new_price
        

    def __del__(self):
        print('Product Destructor Method')
        
        
p1 = Product(1001, "TV", 70000, 1)
p1.showProduct()

print("Price after discount:", p1.applyDiscount())
#print("Price after discount:",Product.applyDiscount(p1))           #--> works

print('--------------')

p2 = Product()
p2.showProduct()



