#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
http://rosalind.info/problems/perm/
Input: positive integer n
Output: The total number of permutations of length n,
        followed by a list of all permutations
"""
def permute(var):
    '''
    Prints all permutations of items in a list    
    '''
    chosen = []
    permutations = []
    permute_helper(var, chosen, permutations)
    
    return permutations
    
    
def permute_helper(var, chosen, permutations):
    '''
    Helper function for permute()
    '''
    if len(var) == 0:
        out = ''
        for item in chosen:
            out += str(item) + ' '
        print(out)
        
    else:
        for num in range(len(var)):
            c = var[num]
            chosen.append(c)
            var.remove(c)

            permute_helper(var, chosen, permutations)
            
            var.insert(num, c)
            chosen.remove(c)
 
       
def factorial(num):
    '''
    Finds the factorial of a number
    '''
    prod = 1
    for i in range(1,num+1):
        prod *= i
    
    return prod
    
n = 5

print(factorial(n))
permute(list(range(1,n+1)))
