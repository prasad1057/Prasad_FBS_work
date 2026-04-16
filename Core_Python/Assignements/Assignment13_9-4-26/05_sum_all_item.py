# 5. Python Program to Sum All the Items in a Dictionary


dict1 = {
    'a': 10,
    'b': 20,
    'c': 30,
    'd': 40
}


total = 0
for key in dict1:
    total += dict1[key]
    
print(total)