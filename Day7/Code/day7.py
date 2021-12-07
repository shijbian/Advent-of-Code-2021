#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 14:32:05 2021

@author: SBIAN6
"""

# Question 1

with open("/Users/SBIAN6/Dropbox/Advent of Code 2021/Day7/Input/day7_puzzle_input.txt","r") as infile:
    input = [ int(x) for x in infile.read().strip().split(',') ]
input.sort()

med = input[int(len(input)/2)]

cost_pos = [abs(x - med) for x in input]

sum(cost_pos)

# Question 2

with open("/Users/SBIAN6/Dropbox/Advent of Code 2021/Day7/Input/day7_puzzle_input.txt","r") as infile:
    input = [ int(x) for x in infile.read().strip().split(',') ]

average = round(sum(input) / len(input)) - 1

cost_pos = [(abs(x - average) + 0)*(abs(x - average) + 1)/2 for x in input]

sum(cost_pos)

