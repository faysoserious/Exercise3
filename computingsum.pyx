#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 23:54:22 2017

@author: grade12
"""
print("import success")


def computingsum(int n):
    cdef int i=0
    cdef double result = 0
    while i < n:
        i = i+1
        result = result + 1/(i**2)

    return result
