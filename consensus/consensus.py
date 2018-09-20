#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
http://rosalind.info/problems/cons/
Finds the consensus of multiple strands of DNA
"""
import sys
sys.path.append('..')
from rosalind import format_fasta, list_format

file = 'rosalind_cons.txt'
fasta = format_fasta(file)

def consensus(strings_dict):
    '''
    Takes in a dict of equal length DNA strands and their IDs
    Returns a consensus string
    '''
    values = list(strings_dict.values())
 
    x = len(values[0])
    
    a = [0] * x
    t = [0] * x
    c = [0] * x
    g = [0] * x
    
    for item in values:
        item = list(item)
        for num in range(x):
            if item[num] == 'A':
                a[num] += 1
            elif item[num] == 'T':
                t[num] += 1
            elif item[num] == 'C':
                c[num] += 1
            elif item[num] == 'G':
                g[num] += 1
    
    out = ''
    for num in range(x):
        high = 0
        val = ''
        
        if a[num] > high:
            val = 'A'
            high = a[num]
        if t[num] > high:
            val = 'T'
            high = t[num]
        if c[num] > high:
            val = 'C'
            high = c[num]
        if g[num] > high:
            val = 'G'
            high = g[num]
        
        out += val
    
    print(out)
    print('A: ' + list_format(a))
    print('C: ' + list_format(c))
    print('G: ' + list_format(g))
    print('T: ' + list_format(t))
        
    
consensus(fasta)