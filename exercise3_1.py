# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 14:35:19 2017

@author: fxie_
"""
import numpy as np
input = np.loadtxt("exercise3_1.txt",dtype ='i',delimiter = ',')
A = input[:,0:3]
b = input[:,3]
x = np.linalg.solve(A,b)
