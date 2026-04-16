# 3. Python Program to Check if a Given Key Exists in a Dictionary or Not


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