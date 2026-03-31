list1 = [10,23,45,65,87,56,32]

max = list1[0]
smax = 0

for i in range(len(list1)):
    if list1[i] > max:
        smax = max
        max = list1[i]
    elif list1[i] > smax:
        smax = list1[i]

print(f'Max:{max} and Second Max:{smax}')