#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 21:44:37 2017

@author: grade12
"""

from distutils.core import setup
from Cython.Build import cythonize

setup(
      ext_modules = cythonize("computingsum.pyx")
      )
