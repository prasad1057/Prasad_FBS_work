li1 = [[ele for ele in range(i * 10 + 1, i * 10 + 11)] for i in range(0,10)]
print(li1)



size = 10
num = size * size

board = []

for i in range(size):
    if i % 2 == 0:
        row = [num - j for j in range(size)]
    else:
        row = [num - size + 1 + j for j in range(size)]
        
    board.append(row)
    num = num - size

# print board
for row in board:
    print(row)