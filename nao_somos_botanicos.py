# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 10:40:08 2017

@author: ygorc
"""


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split



data = pd.read_table("plantinhas.txt", sep=',', header=0, names=["sepal-lenght", "sepal-width", "petal-lenght", "petal-width", "class"])



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#y_pred count(y_pred == y_test)