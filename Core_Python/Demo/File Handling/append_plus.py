with open('\FBS\Core_Python\Demo\File Handling\demo.txt','a+') as fp:
    
    print('Cursor:',fp.tell())
    
    fp.seek(0,0)
    print('Content:',fp.read())
    
    fp.write('\nThis is new one line ')
    fp.seek(0,0)
    print('Content:',fp.read())
    