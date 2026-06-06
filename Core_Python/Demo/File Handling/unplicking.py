import pickle

fp = open('Core_Python/Demo/File Handling/demo.pkl', 'rb')

obj =pickle.load(fp)

print(obj)
fp.close()