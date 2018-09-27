#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
http://rosalind.info/problems/hamm/
Finds the Hamming distance of two equal length strings of DNA
The Hamming distance of two strings is the number of differing symbols
"""

def hamming_distance(strand1, strand2):
    '''
    Returns the number of differing corresponding characters
    between two strings
    '''
    strand1 = strand1
    strand2 = strand2
    count = 0
    
    for num in range(len(strand1)):
        if strand1[num] != strand2[num]:
            count += 1
    
    return count


with open('rosalind_hamm.txt') as f:
    lines = f.readlines()

s1 = lines[0].strip()
s2 = lines[1].strip()

print(hamming_distance(s1,s2))