import threading, time

count = 0


class threadCounter(threading.Thread):

    def __init__(self, lock, threadName):
        '''
        @summary: 初始化对象
        @param lock: 锁对象
        @param threadName: 线程名称
        '''
        super(threadCounter, self).__init__(name=threadName)
        self.lock = lock

    def run(self):
        '''
        @summary: 重写父类的run方法， 在线程启动后执行该方法内的代码
        '''
        global count
        self.lock.acquire()
        for i in range(10000):
            count += 1
        self.lock.release()



lock = threading.Lock()
for i in range(5):
    z = threadCounter(lock, "mythread-{}".format(str(i)))
    print(z.name)
    z.start()
    print(z.ident)

time.sleep(2)
print(count)
