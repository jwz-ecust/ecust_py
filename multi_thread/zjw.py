import threading, time


def doWariting():
    print("starting waiting: ", time.strftime('%H:%M:%S'))
    time.sleep(3)
    print("stop waiting: ", time.strftime('%H:%M:%S'))


def do():
    print("fuck")
    time.sleep(3)
    print("fuck, fuck")

thread1 = threading.Thread(target=doWariting)
thread2 = threading.Thread(target=do)

thread1.start()
thread2.start()
time.sleep(1)
print("start join")
thread1.join()
print("end join")
