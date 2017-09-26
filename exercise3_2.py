# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
input = np.loadtxt("exercise3_2.txt",dtype = float, delimiter = ' ')
xdata = input[:,0]
ydata = input[:,1]
def f3(x, a, b,c,d):
    return a*(x**3) + b*(x**2) + c*(x**1) + d*x**0
def fitted(x):
    abcd = np.polyfit(xdata, ydata, 3)
    return abcd[0]*(x**3) + abcd[1]*(x**2)+ abcd[2]*(x**1) + abcd[3]*(x**0)
x0 = [-10, 0.0, 10]
fittedroot = optimize.root(fitted,x0)
plt.plot(xdata, ydata,"r*")
plt.plot(xdata,fitted(xdata))
plt.plot(fittedroot.x,fitted(fittedroot.x),"go")
plt.show()
