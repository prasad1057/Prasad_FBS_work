# 9. Python Program to Calculate the Number of Words and the Number of Characters Present in a String



def count_words_chars(str1):
    
    # Count words
    words = str1.split()
    word_count = len(words)
    
    # Count characters (including spaces)
    char_count = len(str1)
    
    return word_count, char_count


str1 = str(input("Enter the string: "))

w, c = count_words_chars(str1)

print("Number of words:", w)
print("Number of characters:", c)