'''
1. Create a class Book with members as bid,bname,price and author.Add following
methods:
a. Constructor (Support both parameterized and parameterless)
b. Destructor
c. ShowBook
d. Add static variable count and also maintain count of objects created.
'''



class Book:
    
    count = 0
    
    def __init__(self, book_id=None, book_name=None, price=None, author=None):
        
        Book.count += 1
        
        self.bid = book_id
        self.bname = book_name
        self.price = price
        self.author = author
        
    
    def showBook(self):
        print(f"BOOK ID: {self.bid}\nBook Name: {self.bname}\nPRICE: {self.price}\nAUTHOR: {self.author}")
    
    
    @staticmethod
    def totalBook():
        return Book.count
    
    def __del__(self):
        print('Book Destructor Method')
        

# Parameterized object
b1 = Book(101, "Pokemon Book", 10, "Prasad")        #Values are passed.
b1.showBook()   

print('------------------------')

# Parameterless object
b2 = Book()                         #No values passed — still works because of:book_id=None
b2.showBook()


b3 = Book()
b4 = Book()


print('Total number of Books:',Book.totalBook())
