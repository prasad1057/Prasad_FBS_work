# 8. Write a program to create a duplicate of an existing list. It should not point to same list.


def dupList(list1):
    
    new_list = []
    
    for i in list1:
        new_list.append(i)
        
    return new_list



list1 = [1,2,3,4,5,6,7,8,9,10]

dup = dupList(list1)

print("Original list:", list1)
print("Duplicate list:", dup)

print(id(list1))                #2237358397696
print(id(dup))                  #2237358395776


'''
If both variables point to the same list:

list2 = list1

Then:

list2[0] = 100

Both lists change ❌ (same memory)

But with duplication:

list2 = dupList(list1)

Then:

list2[0] = 100

Only list2 changes ✅

'''
