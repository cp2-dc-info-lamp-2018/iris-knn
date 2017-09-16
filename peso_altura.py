#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 10:56:07 2017

@author: canalli
"""

import matplotlib.pyplot as plt
import numpy as np

peso_homem = 12 * np.random.randn(500) + 70
peso_mulher = 10 * np.random.randn(500) + 60

altura_homem = 15 * np.random.randn(500) + 170
altura_mulher = 8 * np.random.randn(500) + 160

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(peso_homem, altura_homem, c='b', marker='o')
ax1.scatter(peso_mulher, altura_mulher, c='r', marker='x')
ax1.set_xlabel("Peso (Kg)")
ax1.set_ylabel("Altura (cm)")
plt.title("Peso e altura e homens e mulheres")
plt.legend(["Homem", "Mulher"], loc='upper left')
plt.show()
