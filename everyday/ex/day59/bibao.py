def test(func):
    zjw = 'zjw'
    a = 1
    b = 2
    cc = 2
    ccc = 2

    def inner(*args):
        print a, b, cc, ccc
        print func.__closure__
        if len(args) == 0:
            return "null"
        for i in args:
            if not isinstance(i, int):
                return "type error"
        else:
            return func(*args)

    return inner


@test
def my_sum(*args):
    print "in my_sum"
    return sum(args)


@test
def my_average(*args):
    return sum(args) / len(args)


d1 = [1, 2, 3]
d2 = [1, 2, 3, 4, 'i']
d3 = []

print my_sum(*d1)
