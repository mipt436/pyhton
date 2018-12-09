import math as m


class Compl:

    def __init__(self, re, im):
        self.re = re
        self.im = im

    # @re.setter
    def reSetter(self, value):
        self.re = value

    # @im.setter
    def imSetter(self, value):
        self.im = value

    # @re.getter
    def reGetter(self):
        return self.re

    # @im.getter
    def imGetter(self):
        return self.im

    @property
    def absolute(self):
        return m.sqrt(self.re ** 2 + self.im ** 2)

    def out(self):
        print self.re, '+', str(self.im) + 'i'

    def __add__(self, other):
        return Compl(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return Compl(self.re - other.re, self.im - other.im)

    def __div__(self, other):
        x1 = self.re
        y1 = self.im
        x2 = other.re
        y2 = other.im
        return Compl((x1 * x2 + y1 * y2) / (other.absolute() ** 2), (x2 * y1 - x1 * y2) / (other.absolute() ** 2))

    def __mul__(self, other):
        x1 = self.re
        y1 = self.im
        x2 = other.re
        y2 = other.im
        return Compl(x1 * x2 - y1 * y2, x1 * y2 + x2 * y1)


z1 = Compl(input('Re: '), input('Im: '))
z2 = Compl(input('Re: '), input('Im: '))
