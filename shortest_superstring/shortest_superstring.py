#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
http://rosalind.info/problems/long/
Assembles the shortest common superstring from a sequence of
several DNA strings
"""
import sys
sys.path.append('..')
from rosalind import format_fasta


def overlap(s,t):
    '''
    Finds the amount of overlapping characters k between the suffix of a string
    s and the prefix of a string t
    '''
    k = len(s)
    while k > 0:
        if s[-k:] == t[:k]:
            break
        else:
            k -= 1
    return k
    
file = 'rosalind_long.txt'
strings = list(format_fasta(file).values())
merged = []
used = []
var = int(len(strings[0])/2)

while True:
    for s1 in strings:
        for s2 in strings:
            if s1 == s2:
                continue
            else:
                if s1 in used or s2 in used:
                    continue
                else:
                    if overlap(s1,s2) > var:
                        merged.append(s1 + s2[overlap(s1,s2):])
                        used.append(s1)
                        used.append(s2)
    for item in strings:
        if item not in used:
            merged.append(item)
    if len(merged) == 1:
        break
    
    strings = merged
    merged = []
    used = []

print(merged[0])

