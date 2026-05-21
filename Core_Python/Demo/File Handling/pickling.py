import pickle

di = {
    'id':101,
    'name': 'Prasad',
    'sal': 500,
    'dept': 'IT'
}


fp = open('Core_Python/Demo/File Handling/demo.pkl', 'wb')

pickle.dump(di, fp, protocol=pickle.HIGHEST_PROTOCOL)

fp.close()