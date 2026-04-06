# 4. Write a program to reverse the list.


def revList(list1):
    start = 0
    end = len(list1) - 1            # store last index number(i.e 10 value index) = 9
    
    while start < end:
        temp = list1[start]          #store first element in temporary variable
        list1[start] = list1[end]       #swap last element to first
        list1[end] = temp               #swap temporary ele(first ele) to last
        
        start += 1              #increment one by one 
        end -= 1                #decrement one by one
        
    return list1


list1 = [11,22,13,54,35,56,67,8,99,10]

print('Normal List:',list1)
print('Reversed List:',revList(list1))