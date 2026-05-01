def myDecorator(fun):
    pass



@myDecorator            #--> @myDecorator = myDecorator(greet)
def greet():            # this greet passes to above fun 
    print('Good Night!')