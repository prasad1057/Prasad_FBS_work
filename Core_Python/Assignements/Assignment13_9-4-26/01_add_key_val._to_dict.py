# 1. Python Program to Add a Key-Value Pair to the Dictionary.


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