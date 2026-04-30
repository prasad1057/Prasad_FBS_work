li1 = [ele for ele in range(1,11)]
print(li1)


#even number of list
li2 = [ele for ele in range(1,11) if ele % 2 == 0]
print(li2)


#odd number of list
li2 = [ele for ele in range(1,11) if ele % 2 != 0]
print(li2)


#user input list
li3 = [int(input('Enter: ')) for ele in range(1,6)]
print(li3)