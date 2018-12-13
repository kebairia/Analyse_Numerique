#!/usr/bin/env python
from math import *
epsilon = 0.001
def dichotomie(f, a, b):
    g = lambda a,b: (a+b)/2
    if f(a) * f(b) < 0:
        print ("f(%s) x f(%s) < 0 --> there is a solution in [%s,%s]"% (a,b,a,b))
    an = a
    bn = b
    xn = 0
    print ("an\t\t\t bn\t\t\t xn")
    print ("----------------------------------------------------------------------------")
    while (bn-an) > epsilon:
        xn = g(an,bn)
        print (an,'\t\t\t', bn,'\t\t\t', xn)
        if f(xn) < 0:
            an = xn
        elif f(xn) > 0:
            bn = xn
        elif f(xn) == 0:
            return xn
def f(x):
    return x**2 -2  
dichotomie(f,0 ,1)

