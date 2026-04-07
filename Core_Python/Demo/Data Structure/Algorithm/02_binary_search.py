def binarySearch(list1,search_ele):
    
    beg = 0
    end = len(list1) - 1
    
    while (beg <= end):
        print('while loop')                 # 3 times while loop alwayas execute if there is match or dont match
        mid = (beg + end) // 2
        
        if (search_ele == list1[mid]):
            return mid
        
        elif (search_ele >= list1[mid]):
            beg = mid + 1
            
        elif (search_ele <= list1[mid]):
            end = mid - 1
            
    else:
        return -1
    

list1 = [10,20,30,40,50,60,70]

search_ele = int(input('Enter the element to find: '))

result = binarySearch(list1,search_ele)

if (result != -1):
    print(f'{search_ele} is present at index {result}')
    
else:
    print(f'{search_ele} is not present')