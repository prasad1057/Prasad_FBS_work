# 8. Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary



def wordFrequency(str1):

    words = str1.split()

    dict1 = {}

    for word in words:

        if word in dict1:
            dict1[word] += 1
        else:
            dict1[word] = 1

    return dict1


str1 = input("Enter a string: ")

result = wordFrequency(str1)

print("Word Frequency:")
print(result)