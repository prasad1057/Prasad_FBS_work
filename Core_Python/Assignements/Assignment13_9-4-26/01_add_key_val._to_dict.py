# 1. Python Program to Add a Key-Value Pair to the Dictionary.


def userDict():
    
    dict1 = {}
    
    num = int(input('Enter the number of key-value pairs: '))
    
    for i in range(1,num+1):
        key = input('Enter key: ')
        value = input('Enter value: ')
        
        dict1[key] = value
        
    print(dict1.keys())
    print(dict1.values())
    print(dict1.items())
        
    return dict1


result = userDict()
print('User Input Dictionary:',result)




'''
dict1 = {
    'name' : 'Prasad',
    'lastName' : 'Khandagale',
    'email' : 'prasad@gmail.com',
    'address' : 'Panvel'
}

print(dict1)                #{'name': 'Prasad', 'lastName': 'Khandagale', 'email': 'prasad@gmail.com', 'address': 'Panvel'}
print(dict1.keys())         #dict_keys(['name', 'lastName', 'email', 'address'])
print(dict1.values())       #dict_values(['Prasad', 'Khandagale', 'prasad@gmail.com', 'Panvel'])
print(dict1.items())        #dict_items([('name', 'Prasad'), ('lastName', 'Khandagale'), ('email', 'prasad@gmail.com'), ('address', 'Panvel')])

'''