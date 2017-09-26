# -*- coding: utf-8 -*-
# Import numpy dictionary
import numpy as np
# Read the file as numpy vector with two dimension, the values are separated by ','
# Data type is "int"
input = np.loadtxt("exercise3_1.txt",dtype ='i',delimiter = ',')
# A is the first three columns
# [:,0:3] represents all rows of column 0 to 3 
A = input[:,0:3]
# [:,0:3] represents the last column(3) with all rows 
b = input[:,3]
#solve()-function
x = np.linalg.solve(A,b)
