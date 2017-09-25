# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:04:56 2017

@author: fxie_
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
input = np.loadtxt("exercise3_2.txt",delimiter = ' ')
xdata = input[:,0]
ydata = input[:,1]
def f3(x, a, b,c,d):
    return a*x**3 + b*x**2 + c*x**1 + d*x**0
def fitted(x):
    guess = [0, 0,0,0]
    abcd, abcd_covariarance = optimize.curve_fit(f3, xdata, ydata, guess)
    return abcd[0]*x**3 + abcd[1]*x**2+ abcd[2]*x**1 + abcd[3]*x**0

root1 = optimize.fsolve(fitted, xdata[0])
root2 = optimize.root(fitted,xdata[0])
plt.plot(xdata, ydata,"r*")
plt.plot(xdata,fitted(xdata))
plt.show()