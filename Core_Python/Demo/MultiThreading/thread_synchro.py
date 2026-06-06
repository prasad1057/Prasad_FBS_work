import time
from threading import Thread, Lock


def deposit(amt):
    lock.acquire()

    with open(r'd:\FBS\Core_Python\Demo\MultiThreading\balance.txt', 'r') as fp:
        bal = int(fp.read())
        bal += amt

    with open(r'd:\FBS\Core_Python\Demo\MultiThreading\balance.txt', 'w') as fp:
        fp.write(str(bal))

    lock.release()


def withdraw(amt):
    lock.acquire()

    with open(r'd:\FBS\Core_Python\Demo\MultiThreading\balance.txt', 'r') as fp:
        bal = int(fp.read())
        bal -= amt

    with open(r'd:\FBS\Core_Python\Demo\MultiThreading\balance.txt', 'w') as fp:
        fp.write(str(bal))

    lock.release()


lock = Lock()

t1 = Thread(name='Thread1', target=deposit, args=(5000,))
t2 = Thread(name='Thread2', target=withdraw, args=(3000,))

t1.start()
t2.start()