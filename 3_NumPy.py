import numpy as np
import time


def function_hard_to_calculate(arr):
    start = time.time()
    for i in range(10000):
        arr = arr * i
    print 'it took {} seconds to calculate for {}'.format(time.time() - start, type(arr))

    return arr


def my_np_linspace(start, end, number):
    step = float((end - start)) / (number - 1)
    arr = [start + step * i for i in range(number)]
    return arr


np_arr = np.random.random((3, 4, 2))
print np_arr
print type(np_arr)
print 'access a single element: ', np_arr[1, 2, 0]
print 'slice np_arr[1:3, :, 1:]: ', np_arr[1:3, :, 1:]

np_arr = np.linspace(-1000, 1000, 1001)
function_hard_to_calculate(np_arr)

list_arr = [i for i in range(-1000, 1001, 1)]
function_hard_to_calculate(list_arr)

print my_np_linspace(0, -10, 2)
print np.linspace(0, -10, 2)
