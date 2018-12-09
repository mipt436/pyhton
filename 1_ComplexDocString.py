# -*- coding: utf-8 -*-
import math as m
import doctest


# TODO doctest
# Функция для вычисления модуля и аргумента комплексного числа
def cmplx(r, i):
    """
    For given real and imaginary parts of a complex number calculate absolute value and argument.
    Returns a tuple of floats {abs, arg}.

    :param r:  real part of a complex number
    :param i:  imaginary part of a complex number
    :return:   tuple {abs, arg}

    >>> [cmplx(x, x)[0] for x in range(1, 5)]
    [1.4142135623730951, 2.8284271247461903, 4.242640687119285, 5.656854249492381]

    >>> [cmplx(x, x)[1] for x in range(1, 5)]
    [0.7853981633974483, 0.7853981633974483, 0.7853981633974483, 0.7853981633974483]

    >>> cmplx(0, 0)
    Traceback (most recent call last):
        ...
    ValueError: Re cant be 0

    >>> cmplx(0, 1)
    Traceback (most recent call last):
        ...
    ValueError: Re cant be 0

    >>> cmplx(1, 0)
    (1.0, 0.0)

    """
    absolute = m.sqrt(r ** 2 + i ** 2)
    if (r == 0):
        raise ValueError('Re cant be 0')
    else:
        arg = m.atan(i / r)

    return absolute, arg


doctest.testmod()

re_part = int(input('Re: '))
im_part = int(input('Im: '))

props = cmplx(re_part, im_part)

print 'for {} + {}*i: abs = {:.3f}, arg = {:.3f}'.format(re_part, im_part, props[0], props[1])
# А как узнать тип функции, не вызывав ее ни разу
print type(props)