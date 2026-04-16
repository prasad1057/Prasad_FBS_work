# 2. Python Program to Concatenate Two Dictionaries Into One

'''
we can not directly concat two dictionaries using add operator
we have to add one by one element to the third dictionary
'''



dict1 = {
    'id' : 1,
    'name' : 'Prasad',
    'lastName' : 'Khandagale'
}

dict2 = {
    'email' : 'prasad@gmail.com',
    'address' : 'Panvel'
}

result = {}


# Add items from first dictionary
for i in dict1:
    result[i] = dict1[i]
    
# Add items from second dictionary
for j in dict2:
    result[j] = dict2[j]
    
    
print(result)