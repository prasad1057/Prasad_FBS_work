# 5. Python Program to Sort a List According to the Length of the Elements within the list.


def sortList():

    size = len(animals)

    for i in range(1,size):
        
        for j in range(0,size-i):
            if len(animals[j]) > len(animals[j+1]):
                animals[j], animals[j+1] = animals[j+1], animals[j]
                
    return animals


animals = ["cat", "elephant", "dog", "lion", "a", "hi"]

result = sortList()

print("After sorting according to length:")
print(result)