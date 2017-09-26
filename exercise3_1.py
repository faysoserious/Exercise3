# -*- coding: utf-8 -*-

import numpy as np
input = np.loadtxt("exercise3_1.txt",dtype ='i',delimiter = ',')
A = input[:,0:3]
b = input[:,3]
x = np.linalg.solve(A,b)
