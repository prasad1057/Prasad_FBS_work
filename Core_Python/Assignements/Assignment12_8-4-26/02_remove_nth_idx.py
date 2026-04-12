# 2. Python Program to Remove the nth Index Character from a Non-Empty String.

def remove_nth_char(string, n):
    new_string = string[:n] + string[n+1:]
    return new_string

# Input
s = input("Enter a string: ")
n = int(input("Enter index to remove: "))

# Output
result = remove_nth_char(s, n)
print("String after removing character:", result)