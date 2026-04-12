# 8. Print 1 to 100 in Snakes and Ladder pattern

def snake_ladder_pattern(n):
    
    num = 1
    
    for i in range(n):
        
        row = []
        
        for j in range(10):
            row.append(num)
            num += 1
        
        # Reverse every second row (odd index)
        if i % 2 == 1:
            row.reverse()
        
        # Print row
        for k in row:
            print(k, end="\t")
        
        print()


snake_ladder_pattern(10)