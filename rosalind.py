#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
General functions for solving rosalind problems
"""

def format_txt(file):
    '''
    Takes in a .txt file and return a string containing each row of the file
    '''
    data = ''

    with open(file) as f:
        lines = f.readlines()
    
    for line in lines:
        data += line
        
    return format_strand(data)


def format_strand(string):
    '''
    Removes all non nucleotides from a string
    '''
    nucleotides = ['A','C','G','T','U']
    string = list(string)
    
    out = ''
    for item in string:
        if item in nucleotides:
            out += item
    
    return out


def concatenate(var):
    '''
    Concatenates every item from a list into a string
    '''
    out = ''
    for item in var:
        out += str(item)
        
    return out


def list_format(var):
    '''
    Returns a string of every item in a list separated by a space
    '''
    out = ''
    for item in var:
        out += str(item) + ' '
        
    return out


def format_fasta(file):
    '''
    Creates a dict of FASTA IDs and DNA strands from a .txt file
    '''
    fasta_dict = {}
    
    with open(file) as f:
        lines = f.readlines()
    
    for line in lines:
        line = line.strip()
        if '>' in line:
            key = concatenate(list(line)[1:])
            fasta_dict[key] = ''
        else:
            fasta_dict[key] += line
            
    return fasta_dict
    

