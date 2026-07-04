
# 3. Python Program to Check if a Given Key Exists in a Dictionary or Not

def userDict():
    
    dict1 = {}
    num = int(input('ENter the numer of key-value pairs: '))
    
    for i in range(1,num+1):
        key = input(f'Enter key {i}: ')
        value = input(f'Enter value {i}: ')
        
        dict1[key] = value
        
    return dict1


def checkKey(r):
    k = input('Enter key to search: ')
    
    if k in r:
        return 'Yes, key Exist!'
    else:
        return 'Key does not exist!'
    


user_dict = userDict()
print('User Input Dictionary:',user_dict)


result = checkKey(user_dict)
print(result)






'''

def check_key(d, key):
    
    if key in d:
        return "Yes, key exists"
    else:
        return "Key does not exist"


dict1 = {
    'id': 1,
    'name': 'Prasad',
    'lastName': 'Khandagale',
    'email': 'prasad@gmail.com',
    'address': 'Panvel'
}

k = input("Enter key to search: ")

result = check_key(dict1, k)

print(result)



# if k in dict1:
#     print('yes')
# else:
#     print('not')


'''