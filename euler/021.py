#! /usr/bin/env python
import math
from functools import reduce
import operator

def divisors(number):
    '''returns the proper divisors of a number'''
    sq = int(math.ceil(number ** 0.5)) + 1
    smldivs = set()
    for i in range(1, sq):
        if number % i == 0: smldivs.add(i)

    divs = smldivs.copy()
    for i in smldivs:
        divs.add(number / i)
    
    if number != 1: divs.remove(number)
    else: divs.add(1)
    return divs

total = 0
for num in range(2,10000):
    sm = int(reduce(operator.add, divisors(num)))
    cntrsm = int(reduce(operator.add, divisors(sm)))
    if cntrsm == num and sm != num:
        total += num

print(total)
