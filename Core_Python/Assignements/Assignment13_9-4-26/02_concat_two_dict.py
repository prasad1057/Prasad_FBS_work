# 2. Python Program to Concatenate Two Dictionaries Into One

'''
We cannot directly concatenate two dictionaries using the + operator.
Here, we copy each key-value pair into a third dictionary.
'''

def userDict():

    dict1 = {}
    dict1_num = int(input("Enter number of key-value pairs for dict1: "))

    for i in range(dict1_num):
        key = input("Enter key: ")
        value = input("Enter value: ")

        dict1[key] = value

    dict2 = {}
    dict2_num = int(input("Enter number of key-value pairs for dict2: "))

    for i in range(dict2_num):
        key = input("Enter key: ")
        value = input("Enter value: ")

        dict2[key] = value



    add_dict = {}

    # Add items from first dictionary
    for i in dict1:
        add_dict[i] = dict1[i]

    # Add items from second dictionary
    for j in dict2:
        add_dict[j] = dict2[j]

    return add_dict


result = userDict()
print("Concatenated Dictionary:", result)





'''
Method 1: Manual Way (Your Method) ⭐⭐⭐ (Best for understanding)
add_dict = {}

for key in dict1:
    add_dict[key] = dict1[key]

for key in dict2:
    add_dict[key] = dict2[key]

print(add_dict)

-----------------------------------------------

Method 2: Using update() ⭐⭐⭐⭐⭐ (Most Common)
dict1.update(dict2)

print(dict1)

----------------------------------------------

Method 3: Using | (Python 3.9+)
dict3 = dict1 | dict2

print(dict3)


----------------------------------------------

Method 4: Using ** (Dictionary Unpacking)
dict3 = {**dict1, **dict2}

print(dict3)


----------------------------------------------


Method 5: Using copy() + update()
dict3 = dict1.copy()
dict3.update(dict2)

print(dict3)

This keeps the original dictionaries unchanged.
'''
