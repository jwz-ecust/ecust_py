class Pipe(object):
    def __init__(self, func):
        self.func = func

    def __ror__(self, other):
        def generator():
            for obj in other:
                if obj is not None:
                    yield self.func(obj)
        return generator()


def add(n):
    print 'success'
    print n


zjw = Pipe(add)
print type(zjw)
print dir(zjw)
for i in zjw.__ror__('zjw'):
    print i


@Pipe
def even_filter(num):
    return num if num % 2 == 0 else None


@Pipe
def multiply_by_three(num):
    return num * 3


@Pipe
def convert_to_string(num):
    print type(num)
    return 'The Number: %s' % num


@Pipe
def echo(item):
    print type(item)
    return item


def force(sqs):
    print type(sqs)
    for item in sqs:
        print item

# nums = [1,2,3,4,5,6,7,8,9,10]
# force(nums | even_filter | multiply_by_three | convert_to_string | echo)
