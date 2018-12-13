#!/bin/python
from math import *
def derive(func, value):
    h = 0.00000000001
    slope = ((func(value + h) - func(value))/h)
    return ("%f" % slope )
