#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Returns the total number of rabbit pairs that will be present after n months,
if we begin with 1 pair and in each generation, every pair of reproduction-age 
rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
"""

def rabbit_count(n,k):
    '''
    Returns the population of rabbit pairs after n months, if each rabbit 
    reproduces k pairs each month
    Assumes rabbits live indefinitely and reach sexual maturity after one month
    '''
    f1 = 1
    f2 = 0
    
    if n == 1:
        return f1
    
    for item in range(n-1):
        # new population = all rabbits + (mature rabbits * number of offspring)
        f = f1 + (f2 * k)
        f2 = f1
        f1 = f

    return f

print(rabbit_count(5,3))
    
