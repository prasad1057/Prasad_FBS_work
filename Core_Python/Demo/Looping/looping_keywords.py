# In looping we have 4 keywords

# 1. pass   --> to skip/neglect expected idented block error

for i in range(1,6):
    pass


# 2. break  --> to terminate the loop immediately

for i in range(1,6):
    if i == 3:
        break
    print(i)
    

# continue    --> it skip/stop the current iteration and moves to next one

for i in range(1,6):
    if i == 3:
        continue
    print(i)
    

# else   --> execute when loop executed successfully
for i in range(1,6):
    print(i)
else:
    print('Else block executed')
    
for i in range(1,6):
    if i == 4:
        break
    print(i)
else:
    print('Else block executed')
    

for i in range(1,6):
    if i == 4:
        continue
    print(i)
else:
    print('Else block executed')