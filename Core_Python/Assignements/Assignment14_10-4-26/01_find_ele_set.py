# 1. Write a Python program to find elements in a given set that are not in another set.


set1 = {10,20,30,40}
set2 = {20,30,50,60}


res = set1.difference(set2)
print('Elements:',res)