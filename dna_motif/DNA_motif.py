#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
http://rosalind.info/problems/subs/
Finds all locations of s as a substring of t
"""
import sys
sys.path.append('..')
from rosalind import list_format

def substring_locations(s,t):
    '''
    Returns all locations of s as substring of t
    '''
    num = len(t)
    locations = []
    
    for j in range(len(s)-num):
        if s[j:j+num] == t:
            locations.append(j+1)
    
    return locations

file = 'rosalind_subs.txt'

with open(file) as f:
    lines = f.readlines()
s = lines[0].strip()
t = lines[1].strip()



print(list_format(substring_locations(s,t)))
    
