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













def countVowels():

    str1 = input("Enter the string: ")
    vowels = ['a', 'e', 'i', 'o', 'u']

    total_count = 0

    words = str1.split()   # Split string into words

    for word in words:
        count = 0
        for ch in word:
            if ch.lower() in vowels:
                count += 1

        print(f"{word} has {count} vowels")
        total_count += count

    print("Total vowels in the string:", total_count)


countVowels()