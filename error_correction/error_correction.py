'''
http://rosalind.info/problems/corr/
Given: A collection of up to 1000 reads of equal length. Some of these reads 
       were generated with a single-nucleotide error. For each read s in the 
       dataset, one of the following applies:
           s was correctly sequenced and appears in the dataset at least twice 
           
           s is incorrect, it appears in the dataset exactly once, and its 
           Hamming distance is 1 with respect to exactly one correct read

Return: A list of all corrections in the form "[old read]->[new read]". 
'''
import sys
sys.path.append('..')
from rosalind import format_fasta, concatenate


def rev_complement(strand):
    '''
    Returns the reverse complement of a strand of DNA
    '''
    complements = {'A':'T','T':'A','C':'G','G':'C'}
    complement = ''
    
    for item in list(strand):
        complement += complements[item]
    
    return complement[::-1]


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

reads = list(format_fasta('rosalind_corr.txt').values())

# Create a list of correct reads
correct = []
for c1 in range(len(reads)):
    for c2 in range(len(reads)):
        if c1 == c2:
            continue
        else:
            s1 = reads[c1]
            s2 = reads[c2]
            if s1 == s2 or s1 == rev_complement(s2):
                if s1 not in correct:
                    correct.append(s1)
                if s2 not in correct:
                    correct.append(s2)

# Create a list of incorrect reads
incorrect = [r for r in reads if r not in correct]

# For each incorrect read, find the correct read with a hamming distance of 1
corrections = {}
for i in incorrect:
    for c in correct:
        if hamming_distance(i, c) == 1:
            corrections[i] = c
            break
        elif hamming_distance(i, rev_complement(c)) == 1 and i \
        not in corrections.keys():
            corrections[i] = rev_complement(c)
            break

# Print incorrect reads and their corrections
for key, value in corrections.items():
    print(key + '->' + value)

