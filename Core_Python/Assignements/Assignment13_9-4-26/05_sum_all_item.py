# 5. Python Program to Sum All the Items in a Dictionary

def userDict():
    
    dict1 = {}
    num = int(input('Enter the number of key-value pairs: '))
    
    for i in range(1,num+1):
        key = input(f'Enter key {i}: ')
        value = int(input(f'Enter value {i}: '))
        
        dict1[key] = value
        
    print(dict1)
    
    total = 0
    for j in dict1:
        total += dict1[j]
        
    return total

result = userDict()
print('Sum of all Items in Dictionary:',result)