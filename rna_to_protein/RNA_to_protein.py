#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translate RNA into protein
"""
import sys 
sys.path.append('..')
from rosalind import format_txt, concatenate

codons = ['UUU','UUC','UUA','UUG', 'UCU', 'UCC', 'UCA', 'UCG', 'UAU', 'UAC', 
          'UAA', 'UAG', 'UGU', 'UGC', 'UGA', 'UGG', 'CUU', 'CUC', 'CUA', 'CUG',
          'CCU', 'CCC', 'CCA', 'CCG', 'CAU', 'CAC', 'CAA', 'CAG', 'CGU', 'CGC',
          'CGA', 'CGG', 'AUU', 'AUC', 'AUA', 'AUG', 'ACU', 'ACC', 'ACA', 'ACG',
          'AAU', 'AAC', 'AAA', 'AAG', 'AGU', 'AGC', 'AGA', 'AGG', 'GUU', 'GUC',
          'GUA', 'GUG', 'GCU', 'GCC', 'GCA', 'GCG', 'GAU', 'GAC', 'GAA', 'GAG',
          'GGU', 'GGC', 'GGA', 'GGG']

proteins = ['F','F','L','L','S','S','S','S','Y','Y','','','C','C','','W','L',
            'L','L','L','P','P','P','P','H','H','Q','Q','R','R','R','R','I','I',
            'I','M','T','T','T','T','N','N','K','K','S','S','R','R','V','V','V',
            'V','A','A','A','A','D','D','E','E','G','G','G','G']

translate = {}

for num in range(len(codons)):
    translate[codons[num]] = proteins[num]
    
def RNA_to_protein(strand):
    strand = list(strand)
    x = 0
    out = ''
    
    while x < len(strand):
        codon = concatenate(strand[x:x+3])
        out += translate[codon]
        x += 3
        
    return out

file = 'rosalind_prot.txt'

print(RNA_to_protein(format_txt(file)))