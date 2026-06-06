with open(' ','r+') as fp:
    
    print('Cursor Position:',fp.tell())
    
    fp.seek(5,0)
    
    content = fp.read()
    print(content)
    
    print('Cursor Position:',fp.tell())
    
    fp.write('\nABCD')
    print('Cursor Position:',fp.tell())
    
    #fp.seek(0,0)               # if u dont use this then it ownt give anything beacuse the seek(0,0) says that read all conetnt from starting.
    print(fp.read())

