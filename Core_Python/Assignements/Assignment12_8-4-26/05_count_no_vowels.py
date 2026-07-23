# 5. Python Program to Count the Number of Vowels in a String


def countVowels():
    
    str1 = str(input('Enter the string: '))
    vowels = ['a','e','i','o','u']
    
    count = 0
    for i in str1:
        if i.lower() in vowels:
            count += 1
            
    return count


result = countVowels()
print('Number of vowels is string:',result)