from threading import Thread
from time import sleep
def func1():
    for i in range(1, 11):
        print(i)
        sleep(1)

def func2():
    for j in 'abcdefghij':
        print(j)
        sleep(1)

thread1 = Thread(target = func1, daemon=True)
thread2 = Thread(target = func2, daemon=True)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

