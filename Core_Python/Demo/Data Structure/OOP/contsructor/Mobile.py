# WIth Constructor

class Mobile:
    
    def __init__(self, brand, processor, storage, price):
        self.brand = brand
        self.pro = processor
        self.sto = storage
        self.price = price
        
    def getData(self):
        print('Brand:',self.brand)
        print('Processor:',self.pro)
        print('Storage:',self.sto)
        print('Price:',self.price)
        
        

m1 = Mobile('Samsung', 'SnapDragon', '256 GB', 75000)

m2 = Mobile('Moto', 'Intel', '128 GB', 35000)


m1.getData()
print('-----------------')
m2.getData()