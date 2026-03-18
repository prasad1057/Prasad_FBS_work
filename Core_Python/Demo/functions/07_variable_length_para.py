# why --> To pass multiple values to fucntion
# what --> Mention *(astrick) before parameter name in fucntion definition
# how --> Store all passed values in tuple to get individual values use for loop

def add(a,*numbers):
    sum = 0
    
    for sum in numbers:
        sum += sum
    return sum

result = add('a',10,20,30,40)
print('Result',result)