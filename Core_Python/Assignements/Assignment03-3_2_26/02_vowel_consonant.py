# 2. Write a program to input any alphabet and check whether it is vowel or consonant.

# character = input('Enter the character: ')

# vowel = ['a','e','i','o','u','A','E','I','O','U']

# if character in (vowel):
#     print('It is an vowel.')
# else:
#     print('It is not vowel.')



character = input('Enter the character: ')

vowels = ['a','e','i','o','u']

if len(character) == 1 and character.isalpha():     # character.isalpha() --> Ensures input is alphabet
    if character.lower() in (vowels):               # character.lower() --> Converts input to lowercase
        print('It is an vowel')
    else:
        print('It is a cosonant')
else:
    print('Pleasee enter signlee alphbet ')
    