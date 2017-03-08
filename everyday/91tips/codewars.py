from fractions import Fraction


def fibonacci(n):
    a, b = 1, 2
    i = 0
    while i < n:
        a, b = b, a + b
        i += 1
        yield a


result = fibonacci(30)
sum_result = 0
for i in result:
    sum_result += i

print sum_result
