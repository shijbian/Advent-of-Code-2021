#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 23:56:42 2021

@author: SBIAN6
"""

######## Question 1

import numpy as np
import pandas as pd

df = pd.read_csv("~/Dropbox/Advent of Code 2021/Day5/Input/day5_puzzle_input.txt", 
                 sep = " ", 
                 header = None)

#' Parse the x-axis and y-axis of the two locations and save them as the column
#' of the new data frame newDf

loc1 = df[0].str.split(',', expand=True)
loc1.columns = ['loca1_x', 'loca1_y']

loc2 = df[2].str.split(',', expand=True)
loc2.columns = ['loca2_x', 'loca2_y']

newDf = pd.concat([loc1.reset_index(drop=True), loc2.reset_index(drop=True)], axis=1)

newDf['loca1_x'] = pd.to_numeric(newDf['loca1_x'])
newDf['loca1_y'] = pd.to_numeric(newDf['loca1_y'])
newDf['loca2_x'] = pd.to_numeric(newDf['loca2_x'])
newDf['loca2_y'] = pd.to_numeric(newDf['loca2_y'])

#' Create a new column that is the difference of the x-axis
newDf["change_x"] = newDf["loca2_x"] - newDf["loca1_x"]
newDf["change_y"] = newDf["loca2_y"] - newDf["loca1_y"]

#' Create a matrix
#' determine the dimension of the matrix
maxValue = newDf.max(axis = 0)

stor_matrix = np.full((max(maxValue[0], maxValue[2]) + 1,
         max(maxValue[1], maxValue[3]) + 1), 0, 
        dtype = int)


for i in range(newDf.shape[0]):
    temp_matrix = np.full((max(maxValue[0], maxValue[2]) + 1,
         max(maxValue[1], maxValue[3]) + 1), 0, 
         dtype = int)
    if newDf['change_x'][i] == 0 and newDf['change_y'][i] != 0:
        min_y = min(newDf['loca1_y'][i], newDf['loca2_y'][i])
        max_y = max(newDf['loca1_y'][i], newDf['loca2_y'][i]) + 1
        temp_matrix[newDf['loca1_x'][i], min_y:max_y] = 1 
    elif newDf['change_x'][i] != 0 and newDf['change_y'][i] == 0:
        min_x = min(newDf['loca1_x'][i], newDf['loca2_x'][i])
        max_x = max(newDf['loca1_x'][i], newDf['loca2_x'][i]) + 1
        temp_matrix[min_x:max_x, newDf['loca1_y'][i]] = 1
    else:
        next
    
    stor_matrix = stor_matrix + temp_matrix

np.sum(stor_matrix >= 2)

######## Question 2


df = pd.read_csv("~/Dropbox/Advent of Code 2021/Day5/Input/day5_puzzle_input.txt", 
                 sep = " ", 
                 header = None)

#' Parse the x-axis and y-axis of the two locations and save them as the column
#' of the new data frame newDf

loc1 = df[0].str.split(',', expand=True)
loc1.columns = ['loca1_x', 'loca1_y']

loc2 = df[2].str.split(',', expand=True)
loc2.columns = ['loca2_x', 'loca2_y']

newDf = pd.concat([loc1.reset_index(drop=True), loc2.reset_index(drop=True)], axis=1)

newDf['loca1_x'] = pd.to_numeric(newDf['loca1_x'])
newDf['loca1_y'] = pd.to_numeric(newDf['loca1_y'])
newDf['loca2_x'] = pd.to_numeric(newDf['loca2_x'])
newDf['loca2_y'] = pd.to_numeric(newDf['loca2_y'])

#' Create a new column that is the difference of the x-axis
newDf["change_x"] = newDf["loca2_x"] - newDf["loca1_x"]
newDf["change_y"] = newDf["loca2_y"] - newDf["loca1_y"]

#' Create a matrix
#' determine the dimension of the matrix
maxValue = newDf.max(axis = 0)

stor_matrix = np.full((max(maxValue[0], maxValue[2]) + 1,
         max(maxValue[1], maxValue[3]) + 1), 0, 
        dtype = int)


for i in range(newDf.shape[0]):
    temp_matrix = np.full((max(maxValue[0], maxValue[2]) + 1,
         max(maxValue[1], maxValue[3]) + 1), 0, 
         dtype = int)
    if newDf['change_x'][i] == 0 and newDf['change_y'][i] != 0:
        min_y = min(newDf['loca1_y'][i], newDf['loca2_y'][i])
        max_y = max(newDf['loca1_y'][i], newDf['loca2_y'][i]) + 1
        temp_matrix[newDf['loca1_x'][i], min_y:max_y] = 1 
    elif newDf['change_x'][i] != 0 and newDf['change_y'][i] == 0:
        min_x = min(newDf['loca1_x'][i], newDf['loca2_x'][i])
        max_x = max(newDf['loca1_x'][i], newDf['loca2_x'][i]) + 1
        temp_matrix[min_x:max_x, newDf['loca1_y'][i]] = 1
    elif newDf['change_x'][i] != 0 and newDf['change_y'][i] != 0 and abs(newDf['change_x'][i]) == abs(newDf['change_y'][i]):
        
        move_dir = np.sign(newDf['loca2_y'][i] - newDf['loca1_y'][i])
        if newDf['loca2_x'][i] > newDf['loca1_x'][i]:
            location_x = newDf['loca1_x'][i]
            location_y = newDf['loca1_y'][i]
            
            while location_x <= newDf['loca2_x'][i]:
                temp_matrix[location_x, location_y] = 1
                location_x = location_x + 1
                location_y = location_y + 1*move_dir
        else:
            location_x = newDf['loca1_x'][i]
            location_y = newDf['loca1_y'][i]
            
            while location_x >= newDf['loca2_x'][i]:
                temp_matrix[location_x, location_y] = 1
                location_x = location_x - 1
                location_y = location_y + 1*move_dir

    else:
        next
    
    stor_matrix = stor_matrix + temp_matrix

np.sum(stor_matrix >= 2)
