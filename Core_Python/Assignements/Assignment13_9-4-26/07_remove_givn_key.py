# 7. Python Program to Remove the Given Key from a Dictionary

def userDict():
    
    dict1 = {}
    num = int(input('ENter the numer of key-value pairs: '))
    
    for i in range(1,num+1):
        key = input(f'Enter key {i}: ')
        value = input(f'Enter value {i}: ')
        
        dict1[key] = value
        
    print(dict1)
    
    
    remove_key = input("Enter key to remove: ")
    dict1.pop(remove_key)
    
    return dict1

user_dict = userDict()
print('User Input Dictionary:',user_dict)

