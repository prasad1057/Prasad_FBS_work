def linearSearch(list1,search_ele):
    for i in range(0,len(list1)):
        if search_ele == list1[i]:      # check condition if our element is equal to current value of list
            return i                    #it return the element that u have to search

    else:
        return -1


list1 = [12,34,21,56,78,43,55,99,76,41]
ele = int(input('Enter the number that u want to search: '))

result = linearSearch(list1,ele)

if result != -1:
    print(f'{ele} is present at index {result}')
else:
    print(f'{ele} is not present')
    
    
    
#------------------------------------------------------------------- 
## Search in List of strings
    
def linearSearch2(names,search_key):
    for i in range(0,len(names)):
        if search_key == names[i]:
            return i
        
    else:
        return -1
    
names = ['prasad','durvesh','nikhil','pranav','vishal']

key = 'nikhil'

result = linearSearch2(names,key)

if result != -1:
    print(f'{key} is present at index {result}')
else:
    print(f'{key} is not present')