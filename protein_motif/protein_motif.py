#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Find the locations of the N-glycosylation motif in a protein
"""
import requests

def find_motif(strand):
    '''
    Takes in a protein string and returns the number of times that a certain
    motif is present
    '''
    locations = []
    for ind in range(len(strand)-4):
        s = strand[ind:ind+4]
        if motif_present(s):
            locations.append(ind+1)
    
    out = ''
    for item in locations:
        out += str(item) + ' '
    
    return out

def motif_present(s):
    '''
    Checks if a string matches the N-glycosylation protein motif
    '''
    if s[0] == 'N':
        if s[1] != 'P':
            if s[2] == 'S' or s[2] == 'T':
                if s[3] != 'P':
                    return True
    return False

def format_list(var):
    '''
    Formats the items of a list into a string
    '''
    out = ''
    for item in var:
        out += item
    out.replace("'","")    
    return out


def format_protein(protein):
    '''
    Obtains and formats a protein string given an access ID
    '''
    url = 'https://www.uniprot.org/uniprot/{}.fasta'
    sequence = str(requests.get(url.format(protein)).content).split('\\n')[1:]
    return format_list(sequence)



file = 'rosalind_mprt.txt'
with open(file, 'r') as f:
    proteins = f.readlines()

for protein in proteins:
    protein = protein.strip()

    locations = find_motif(format_protein(protein))
    if len(locations):
        print(protein)
        print(locations)
        

