# 7. Python Program to Find the Intersection of Two Lists

def intersection_lists(list1, list2):
    
    result = []
    
    for i in list1:
        if i in list2 and i not in result:
            result.append(i)
    
    return result


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

inter = intersection_lists(list1, list2)

print("Intersection of two lists:", inter)