# -*- coding: utf-8 -*-
import sys
import time


def timer(f):
    def tmp(n):
        t = time.time()
        res = f(n)
        print "Время выполнения функции %s: %f" % (str(f), (time.time() - t))
        return res

    return tmp

def memoize(f):
    cache = {}

    def decorate(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = f(n)
            return cache[n]
    return decorate

# TODO не работает если убрать комментарий
# @timer
def f(n):
    if n in d:
        return d[n]
    if n < 2:
        return n
    fib = f(n - 1) + f(n - 2)
    d[n] = fib
    return fib


d = {}
max_n = 4190
max_default_depth = sys.getrecursionlimit()
sys.setrecursionlimit(10 * max_default_depth)

n = max_n

print timer(f)(n)
# print "fib({}) = {}".format(n, f(n), (time.time() - start))
# print 'calculated in {} seconds'.format(time.time() - start)
