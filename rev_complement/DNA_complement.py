#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
http://rosalind.info/problems/revc/
Returns the reverse complement of a strand of DNA
"""
import sys
sys.path.append('..')
from rosalind import format_txt, concatenate


def rev_complement(strand):
    '''
    Returns the reverse complement of a strand of DNA
    '''
    complements = {'A':'T','T':'A','C':'G','G':'C'}
    complement = ''
    
    for item in list(strand):
        complement += complements[item]
    
    return complement[::-1]

file = 'rosalind_revc.txt'

print(rev_complement(format_txt(file)))