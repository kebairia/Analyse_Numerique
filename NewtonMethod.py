#!/usr/bin/env python
# TODO: create all the condition that the prof mentioned earlier.
import math
# epsilon
EPSILON = 10**-15
def newton(f, df,startingGuess):
    """
	┌───────────────────────────────┐
	│	-~:NEWTON METHOD:~-	│
	└───────────────────────────────┘
    	Usage:
    	      f  : is the principale function [ f(x) ]
    	      df : is derivative of "f" [ df/dx or f`(x)]
"""
    xn = startingGuess
    while True:
        xn_1 = xn - (f(xn)/df(xn))
        # Critere D'arret
        if abs(xn_1 - xn) < EPSILON:
            return xn_1
        xn = xn_1

def f(x):
    return x**2 - 2
def df(x):
    return 2*x 
print (newton.__doc__)
print (newton(f,df,2))
