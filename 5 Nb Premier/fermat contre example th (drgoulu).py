#!/usr/bin/env python
# coding: utf8
"""
generate wrong counter-examples of Fermat's theorem
see http://www.drgoulu.com/2016/03/25/contre-exemples-au-theoreme-de-fermat-wiles/
"""
from __future__ import print_function, division
import itertools

__author__ = "Philippe Guglielmetti"

def check_fermat(a,b,p,m=[2,3,5]):
    """
    :param a,b,p: integers
    :param m: list of integer (primes) to check for modularity correctness
    :return: integer c and float relative precision of a^p+b^p=c^p
        or (false,integer) if sum is wrong modulo m
    """
    left=float(a**p+b**p)
    c=int(round(left**(1/p)))
    if c==a: # b is too small
        return False,0
    for m in m: #parity check
        if (a%m + b%m)%m != c%m: 
            return False,m
    right=float(c**p)
    e=abs(left-right)/left # relative precision
    return c,e

print(check_fermat(1782,1841,12,[])) # 1922 Cohen, Simpsons
print(check_fermat(3987,4365,12,[2])) # 4472 Cohen, Simpsons
print(check_fermat(48767,24576,4,[2])) #49535^4 (5.1023769743e-16) DrG

for p in itertools.count(3): #powers infinite loop
    emin=1e-9 # min precision of first counter-example at this power
    print('p=%d...'%p)
    for a in range(3,10000):
        for b in range(1,a):
            c,e=check_fermat(a,b,p)
            if c and e<emin: #only display results that improve precision
                emin=e
                print('%d^%d + %d^%d = %d^%d (%s)'%(a,p,b,p,c,p,e))