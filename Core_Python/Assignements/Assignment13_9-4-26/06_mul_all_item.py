# 6. Python Program to Multiply All the Items in a Dictionary


dict1 = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}

total = 1

for key in dict1:
    total *= dict1[key]
    
print(total)