import threading
import time

mutex = threading.Semaphore(1)

def ps1():
    while True:
        mutex.acquire()
        print(1)
        mutex.release()
        time.sleep(.5)


def ps2():
    while True:
        mutex.acquire()
        print(2)
        mutex.release()
        time.sleep(.5)

t1 = threading.Thread(target=ps1)
t2 = threading.Thread(target=ps2)
t1.start()
t2.start()