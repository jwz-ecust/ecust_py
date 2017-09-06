import threading


# lock = threading.Lock()
# lock.acquire()
# lock.acquire()
# lock.release()
# lock.release()


rLock = threading.RLock()
rLock.acquire()
rLock.acquire()
rLock.release()
# rLock.release()
