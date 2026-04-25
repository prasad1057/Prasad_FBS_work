# Without Constructor

'''
class Book:
    
    def setData(self, book_id, book_author, book_price):
        self.id = book_id
        self.author = book_author
        self.price = book_price
        
    
    def getData(self):
        print('Book ID:',self.id)
        print('Book Author:',self.author)
        print('Book Price:',self.price)
        
        
obj1 = Book()
obj1.setData(111, 'Prasakk', 2000)

obj2 = Book()
obj2.setData(222, 'Karankk', 5000)


obj1.getData()
print('------------')
obj2.getData()

'''

# WIth Constructor

class Book:
    
    def __init__(self,  book_id, book_author, book_price):
        self.id = book_id
        self.author = book_author
        self.price = book_price
        
    
    def getData(self):
        print('Book ID:',self.id)
        print('Book Author:',self.author)
        print('Book Price:',self.price)
        
        
b1 = Book(111, 'Prasakk', 2000)
b1.getData()