# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Part 1

import numpy as np
import pandas as pd

df = pd.read_csv("~/Dropbox/Advent of Code 2021/Day1/Input/day1_puzzle_input.txt", 
                 sep = " ", 
                 header = None)

arr = np.zeros(df.shape[0])
pre = df.iloc[0]

for i in range(1, df.shape[0]):
    arr[i] = df.iloc[i] - pre
    pre = df.iloc[i]
    
np.sum(arr > 0)

# Part 2
arr = np.array([])
pre = df.iloc[0] + df.iloc[1] + df.iloc[2]

for i in range(1, df.shape[0] - 2):
    arr = np.append(arr, [df.iloc[i] + df.iloc[i+1] + df.iloc[i+2] - pre])
    pre = df.iloc[i] + df.iloc[i+1] + df.iloc[i+2]
    
np.sum(arr > 0)