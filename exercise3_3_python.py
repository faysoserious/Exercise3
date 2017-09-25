#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 11:29:06 2017

@author: grade12
"""


def computingsum(n):

    i=0
    sumresult = 0
    while i<n:
        i = i+1
        sumresult = sumresult + (1/(i**2))
    return sumresult
        
