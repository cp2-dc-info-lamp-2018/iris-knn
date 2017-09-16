#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 09:49:22 2017

@author: canalli
"""
import numpy as np
from pprint import pprint

m = 5
n = 5

#a = np.random.randint(-10, 10, size=(n))
#b = np.random.randint(-10, 10, size=(n))

def distancia (a, b, n):
    c = 0
    for i in range (n):
        c = (a[i]-b[i])**2 + c
    d = np.sqrt(c)
    return d 

def dist_par_a_par (A, m, n):   
    D = np.zeros((m,m))
    for i in range (m):
        for j in range (m):
            D[i,j] = distancia(A[i], A[j], n)
    return D

A = np.random.rand(m, n)
pprint(A)

D = dist_par_a_par(A, m , n)
pprint(D)



