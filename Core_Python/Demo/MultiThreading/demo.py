import time

from threading import Thread

def fun1(str):
    for i in str:
        print(i, end =' ', flush=True)
        time.sleep(1)
        
def fun2(str):
    for j in str:
        print(j, end = ' ', flush=True)
        time.sleep(1)
        

t1 = Thread(name='thread1', target=fun1, args=('1111111111111', ))
t2 = Thread(name='thread2', target=fun2, args=('2222222222222', ))

t1.start()
t2.start()