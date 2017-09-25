#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print("import success")


def computingsum(int n):
    cdef int i=0
    cdef double result = 0
    while i < n:
        i = i+1
        result = result + 1/(i**2)

    return result
