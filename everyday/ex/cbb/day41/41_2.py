def fileter(n):
    for i in n:
        if i%3==0:
            yield i

def force(sqs):
    print type(sqs)
    for item in sqs: print item

force(range(100)|fileter)