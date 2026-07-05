# 2. Write a Python program to remove the intersection of a second set with a first set.

set1 = {10,20,30,40}
set2 = {20,30,50,60}

set1.difference_update(set2)

print(set1)