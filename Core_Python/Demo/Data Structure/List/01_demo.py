# 1. Structure = []

list1 = [10,20,30,40,50]

print(type(list1))
print(list1)


# 2. Type of Data = Heterogeneous
list2 = [10,20,3.14,'Prasadk']
print(type(list2))
print(list2)


# 3. Sequence = ordered


# 4 . Changable = Mutable
print(id(list1))
print(id(list2))

list2[0] = 50
print(id(list2))
print(type(list2))
print(list2)
print(list2[0])