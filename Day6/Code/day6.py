#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 03:50:22 2021

@author: SBIAN6
"""

# list_pre_day = [1,1,1,1,1,5,1,1,1,5,1,1,3,1,5,1,4,1,5,1,2,5,1,1,1,1,3,1,4,5,1,1,2,1,1,1,2,4,3,2,1,1,2,1,5,4,4,1,4,1,1,1,4,1,3,1,1,1,2,1,1,1,1,1,1,1,5,4,4,2,4,5,2,1,5,3,1,3,3,1,1,5,4,1,1,3,5,1,1,1,4,4,2,4,1,1,4,1,1,2,1,1,1,2,1,5,2,5,1,1,1,4,1,2,1,1,1,2,2,1,3,1,4,4,1,1,3,1,4,1,1,1,2,5,5,1,4,1,4,4,1,4,1,2,4,1,1,4,1,3,4,4,1,1,5,3,1,1,5,1,3,4,2,1,3,1,3,1,1,1,1,1,1,1,1,1,4,5,1,1,1,1,3,1,1,5,1,1,4,1,1,3,1,1,5,2,1,4,4,1,4,1,2,1,1,1,1,2,1,4,1,1,2,5,1,4,4,1,1,1,4,1,1,1,5,3,1,4,1,4,1,1,3,5,3,5,5,5,1,5,1,1,1,1,1,1,1,1,2,3,3,3,3,4,2,1,1,4,5,3,1,1,5,5,1,1,2,1,4,1,3,5,1,1,1,5,2,2,1,4,2,1,1,4,1,3,1,1,1,3,1,5,1,5,1,1,4,1,2,1]
list_pre_day = [3,4,3,1,2]
day = 80

# Part I:
    
for i in range(day):
    
    # Count the how many days are 0 in the previous day
    count_zero = sum(map(lambda x : x==0, list_pre_day))
    append_list = [8] * count_zero
    
    # deduct one from current values from the list    
    list_today = [(x - 1) for x in list_pre_day]
    
    # replace the value -1 with 6, these are the values that previous day was 0
    list_today = [6 if el==-1 else el for el in list_today]
    
    # Append 8 to the end of today's list
    list_today = list_today + append_list
    
    # today becomes yesterday
    list_pre_day = list_today
    

print(len(list_pre_day))
   
# Part II:
    
list_pre_day = [3,4,3,1,2]
day = 256
len_total = 0

    
for i in range(day):
    
    # Count the how many days are 0 in the previous day
    count_zero = sum(map(lambda x : x==0, list_pre_day))
    append_list = [8] * count_zero
    
    # deduct one from current values from the list    
    list_today = [(x - 1) for x in list_pre_day]
    
    # replace the value -1 with 6, these are the values that previous day was 0
    list_today = [6 if el==-1 else el for el in list_today]
    
    # Append 8 to the end of today's list
    list_today = list_today + append_list
    
    # today becomes yesterday
    list_pre_day = list_today
    len_total = len_total + len(list_pre_day)

print(len_total) 

# https://www.reddit.com/r/adventofcode/comments/r9z49j/2021_day_6_solutions/
# the_rainman

# Part 1 Solution

fish = dict()
days = 80
with open("/Users/SBIAN6/Dropbox/Advent of Code 2021/Day6/Input/day6_puzzle_input.txt","r") as infile:
    counters = [ int(x) for x in infile.read().strip().split(',') ]
for i in range(9):
    fish[i] = counters.count(i)
for i in range(days):
    fish[(i+7)%9] += fish[i%9]
print(sum(fish.values()))

# Part 2 Solution
days = 256
for i in range(80, days):
    fish[(i+7)%9] += fish[i%9]
print(sum(fish.values()))