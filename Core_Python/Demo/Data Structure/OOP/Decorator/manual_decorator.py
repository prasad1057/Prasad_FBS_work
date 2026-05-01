def greet():
    print('Good Night!')
    
def myDecorator(fun):           #fun = greet
    print('This is my Decorator.')
    fun()               # fun = greet
    print('End of my Decorator.')
    
    
# greet()                 #Good Night!

myDecorator(greet)
    