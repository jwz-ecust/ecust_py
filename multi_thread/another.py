import threading, time, random

count = 0
lock = threading.Lock()


def doadd():
    global count, lock
    lock.acquire()
    for i in range(10000):
        count = count + 1
    lock.release()


for i in range(5):
    threading.Thread(target=doadd, args=(), name="thread-"+str(i)).start()
    print(threading.Thread.ident)
    print(threading.Thread.name)

time.sleep(2)
print(count)
