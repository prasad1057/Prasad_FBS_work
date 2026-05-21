with open('\FBS\Core_Python\Demo\File Handling\demo.txt','w+') as fp:
    
    print('Cursor:',fp.tell())
    
    fp.write("This is the another new line")
    
    fp.seek(0,0)
    
    content = fp.read()
    print('Content:',content)
    print('Cursor:',fp.tell())