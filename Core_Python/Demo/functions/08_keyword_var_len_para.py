# why --> To pass multiple values with attribute name.
# what --> Mention *(astrick) before parameter name in function definition
# how --> Store values & attribute name in dictionary format. Use for loop to iterate ietms from dict.items()

def emp(**data):
    print(data)
    
emp(id=101,name='ABC',sal=3500)



def emp(**data):
    for key,val in data.items():
        print(f'{key}:{val}')
        
emp (id=201,name='karan',sal=500) 



def emp(id,name,sal=0,dept='',age=None, add='', email='', gender=''):
    print('ID:',id)
    print('NAME:',name)
    print('Salary:',sal)
    print('Department:',dept)
    print('AGE:',age)
    print('ADDRESS:',add)
    print('Email:',email)
    print('Gender:',gender)
    
emp(301,'prasad',gender='Male',dept='Tester')



def dummy(*args,**kwargs):
    print('Arguments:',args)
    print('Keyword Arguments:',kwargs)
    
dummy(10,20,30,40,id=501,name='xyz',sal=3000)