from functools import wraps

def memoize(funciton):
    memo = {}
    @wraps(funciton)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = funciton(*args)
            memo[args]=rv
            return rv
    return wrapper

@memoize
def fibonacci(n):
    if n<2: return n
    return fibonacci(n-1)+fibonacci(n-2)


a=fibonacci(10)
print dir(a)