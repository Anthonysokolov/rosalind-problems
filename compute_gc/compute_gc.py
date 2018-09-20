#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
http://rosalind.info/problems/gc/
Compute the GC content of a strand of DNA
"""
from rosalind import txt_to_list

def compute_gc(string):
    '''
    Returns the ratio of GC nucleotides in a string of DNA
    '''
    var = list(string)
    count = 0
    for item in var:
        if item == 'G':
            count += 1
        elif item == 'C':
            count += 1
    
    return count/len(string)
  

print(txt_to_list('rosalind_gc.txt'))
