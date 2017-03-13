from functools import wraps
import time
def benchmark(func):
    """
    A decorator that prints the time a function takes to exucute.
    """
    @wraps(func)
    def wrapper(*args,**kwargs):
        t = time.clock()
        res = func(*args,**kwargs)
        print func.__name__,time.clock()-t
        return res
    return wrapper

def logging(func):
    """
    A decorator that logs the activity of the script.
    (it actually just prints it, but it could be logging)
    """
    @wraps(func)
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)
        print func.__name__,args,kwargs
        return res
    return wrapper

def counter(func):
    """
    A decorator that counts and prints the number of times a function has been executed.
    """
    @wraps(func)
    def wrapper(*args,**kwargs):
        wrapper.count = wrapper.count + 1
        res = func(*args,**kwargs)
        print "{0} has been used: {1}x".format(func.__name__, wrapper.count)
        return res
    wrapper.count = 0
    return wrapper


@counter
@benchmark
@logging
def reverse_string(string):
    return str(string)


print reverse_string("Able was I ere I saw Elba")
