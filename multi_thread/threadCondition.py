import threading
import time


class Hider(threading.Thread):
    def __init__(self, cond, name):
        super(Hider, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):

        self.cond.acquire()       # 获取锁
        print(self.name + "：我已经把眼睛蒙上了")
        time.sleep(1)
        self.cond.notify()        # 唤醒一个挂起的线程
        self.cond.wait()          # 释放内部所占用的锁，直至收到通知被唤醒或者超时

        print(self.name, "：我找到你了 =。=")
        self.cond.notify()
        self.cond.wait()
        print(self.name + "：我赢了，哈哈")
        self.cond.release()



class Seeker(threading.Thread):
    def __init__(self, cond, name):
        super(Seeker, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        self.cond.acquire()
        self.cond.wait()
        time.sleep(1)
        print(self.name + ": 我已经藏好了， 你快来找我吧")
        time.sleep(1)
        self.cond.notify()
        self.cond.wait()
        self.cond.notify()

        print(self.name + ": 被你找到了，Fuck You!")

        self.cond.release()



cond = threading.Condition()
seeker = Seeker(cond, "seeker")
hider = Hider(cond, "hider")
seeker.start()
hider.start()
