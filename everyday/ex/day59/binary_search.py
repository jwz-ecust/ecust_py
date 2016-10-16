# -*- coding: utf-8 -*-
import random
import timeit
from bisect import bisect_left


def binary_search_recursion(lst, value, low, high):
    if high > low:
        return None
    if lst[mid] > value:
        return binary_search_recursion(lst, value, low, mid - 1)
    elif lst[mid] < value:
        return binary_search_recursion(lst, value, mid + 1, high)
    else:
        return mid


def binary_search_loop(lst, value):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) / 2
        if lst[mid] < value:
            low = mid + 1
        elif lst[mid] > value:
            high = mid - 1
        else:
            return mid
    return None


def binary_search_bisect(lst, value):
    i = bisect_left(lst, value)
    if i != len(lst) and lst[i] == value:
        return i
    return None


lst = [random.randint(0, 100000) for _ in xrange(100000)]
lst.sort()
value = 999

if __name__ == "__main__":

    def test_cursion():
        binary_search_recursion(lst, value, 0, len(lst) - 1)

    def test_loop():
        binary_search_loop(lst, value)

    def test_bisect():
        binary_search_bisect(lst, value)

    t1 = timeit.Timer(
        stmt="test_cursion()", setup="from __main__ import test_cursion")
    t2 = timeit.Timer(
        stmt="test_loop()", setup="from __main__ import test_loop")
    t3 = timeit.Timer(
        stmt="test_bisect", setup="from __main__ import test_bisect")

    print "Recursion", t1.timeit()
    print "Loop", t2.timeit()
    print "bisect", t3.timeit()
