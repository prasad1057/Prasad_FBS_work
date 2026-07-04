'''
Method	                                              Purpose
----------------------------------------------------------------------------------------------------------
add()                               -->      	Add one element
clear()	                            -->         Remove all elements
copy()	                            -->         Create a copy
difference()	                    -->         Return different elements
difference_update()	                -->         Remove common elements from original set
discard()	                        -->         Remove element (No Error)
intersection()	                    -->         Return common elements
intersection_update()	            -->         Keep only common elements
isdisjoint()	                    -->         Check if no common elements
issubset()	                        -->         Check if one set is inside another
issuperset()	                    -->         Check if one set contains another
pop()	                            -->         Remove random element
remove()	                        -->         Remove element (Error if missing)
symmetric_difference()	            -->         Return uncommon elements
symmetric_difference_update()       --> 	    Update with uncommon elements
union()	                            -->         Return all unique elements
update()	                        -->         Add all elements to original set



1. add() vs update()
add()    → Adds one element.
update() → Adds multiple elements.


2. remove() vs discard()
remove()  → Error if element doesn't exist.
discard() → No error if element doesn't exist.


3. difference() vs difference_update()
difference()        → Returns a new set.
difference_update() → Changes the original set.


4. intersection() vs intersection_update()
intersection()        → Returns a new set.
intersection_update() → Modifies the original set.


5. union() vs update()
union()  → Returns a new set.
update() → Modifies the original set.
'''



set1 = {10,20,30,40,50}
set2 = {30,40,50,60}
set3 = {40,50}
set4 = {70,80}

print(type(set1))


#1. add()   --> Add a single element
set1.add(100)
print('Add:',set1)


# 2. clear() --> Remove all elements from the set
temp = set1.copy()
temp.clear()
print('Clear:',temp)


# 3. copy() --> Create a copy of the set
copy_set = set1.copy()
print('Copy Set:',copy_set)


#4. difference()            --> Returns elements present in set1 but not in set2
res = set1.difference(set2)
print('Difference:',res)


#5. difference_update()         --> Remove common elements from original set
temp = set1.copy()
temp.difference_update(set2)
print('Difference Update:',set2)


#6. discard()       --> Remove element id present (No Error if not found)
temp = set1.copy()
temp.discard(50)
print('Discard:',temp)


#7. intersection()      --> Returns common elements from both sets
res = set1.intersection(set2)
print('Intersection:',res)


#8. intersection_update()       --> Keep only common elements in original set
temp = set1.copy()
temp.intersection_update(set2)
print('Intersection Update:',temp)


#9. isdisjoint()        --> Returns True if no common elements
res = set1.isdisjoint(set4)
print('IsDisJoint:',res)


#10. issubset()         --> Returns True if all elements of set3 are in set2
res= set3.issubset(set2)
print('IsSubset:',res)


#11. issuperset()       --> Returns True if set2 contains all elements of set3
res = set2.issuperset(set3)
print('IsSuperset:',res)


#12. pop()      --> Remove a random element
temp= set1.copy()
print('Pop Element:',temp.pop())
print('After removing pop element:',temp)


#13. remove()       --> Remove given element (Error if element not found)
temp = set1.copy()
temp.remove(50)
print('Remove:',temp)


#14. symmetric_difference()     --> Returns elements present in either set1 but not both
res = set1.symmetric_difference(set2)
print('Symmetric Difference:',res)


#15. symmetric_difference_update()      --> Update original set with symmetric difference
temp = set1.copy()
temp.symmetric_difference_update(set2)
print('Symmetric Difference Update:',res)


#16. union()        --> Returns all unique elements from both sets
res = set1.union(set2)
print('Union:',res)


#17. update()       --> Add all elements of set2 into set1
temp = set1.copy()
temp.update(set2)
print('Update:',temp)