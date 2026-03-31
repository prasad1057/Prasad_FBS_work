
# Q. WAP to find maximum number from list

list6 = [30,60,70,80,10,20,40,55]

max = list6[0]

for i in range(1,len(list6)):
    if list6[i] > max:
        max = list6[i]
print(max)
    