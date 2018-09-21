#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
http://rosalind.info/problems/grph/
Input: A collection of DNA strings
Output: Each pair of strings with overlapping edges of length k
"""
import sys
sys.path.append('..')
from rosalind import format_fasta, concatenate

fasta = format_fasta('rosalind_grph.txt')


def overlap(k):
    '''
    Finds every pair of strings with overlapping edges of length k
    '''
    for key0 in fasta.keys():
        for key1 in fasta.keys():
            if key0 == key1:
                continue
            elif fasta[key0][-k:] == fasta[key1][:k]:
                print(key0, key1)


k = 3
overlap(k)
