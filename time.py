#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import timeit

cy = timeit.timeit('computingsum.computingsum(10000)',setup='import computingsum',number =500)
py = timeit.timeit('exercise3_3_python.computingsum(10000)',setup='import exercise3_3_python',number =500)

print(cy, py)
print('Cython is {} faster'.format(py-cy))
