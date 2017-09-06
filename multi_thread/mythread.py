import threading, time, random
count = 0


class Counter(threading.Thread):
    def __init__(self, lock ,threadName):
        super(Counter, self).__init__(name=threadName)
        self.lock = lock

    def run(self):
        global count
        self.lock.acquire()
        for i in range(10000):
            count = count + 1
        self.lock.release()


lock = threading.Lock()
for i in range(5):
    Counter(lock, "thread-{}".format(str(i))).start()
time.sleep(2)
print(count)
