# 8. Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary



def wordFrequency():

    str1 = input("Enter a string: ")
    words = str1.split()

    dict1 = {}

    for word in words:

        if word in dict1:
            dict1[word] += 1
        else:
            dict1[word] = 1

    return dict1



result = wordFrequency()
print("Word Frequency:",result)
