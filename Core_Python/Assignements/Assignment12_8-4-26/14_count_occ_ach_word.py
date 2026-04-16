# 14. Python Program to count the occurrences of each word in a string.



def count_word_occurrences(str1):
    
    words = str1.split()
    result = {}
    
    for w in words:
        if w in result:
            result[w] += 1
        else:
            result[w] = 1
    
    return result


str1 = input("Enter the string: ")

counts = count_word_occurrences(str1)

print("Occurrences of each word:")
for word in counts:
    print(word, ":", counts[word])