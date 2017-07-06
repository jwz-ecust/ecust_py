class SpamException(Exception):
    pass


def write():
    while True:
        try:
            w = (yield)
        except SpamException:
            print("***fuck***")
        else:
            print(">> ", w)


def writer_wrapper(core):
    yield from core


w = writer_wrapper(write())
w.send(None)


for i in [1,2,3,4,9,'zjw',10]:
    if isinstance(i, str):
        w.throw(SpamException)
    else:
        w.send(i)
