import threading


def dead_loop():
    while True:
        pass


# dead_loop()

t = threading.Thread(target=dead_loop)
t.start()

# t.join()
