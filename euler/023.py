#! /usr/bin/env python
import math
from functools import reduce
import operator

def divisors(number):
    '''returns the proper divisors of a number'''
    sq = int(math.ceil(number ** 0.5))+1
    smldivs = set()
    for i in range(1, sq):
        if number % i == 0: smldivs.add(i)

    divs = smldivs.copy()
    for i in smldivs:
        divs.add(number / i)
    
    if number != 1: divs.remove(number)
    else: divs.add(1)
    return divs

def smdiv(number):
    '''returns the sum of the divisors'''
    return reduce(operator.add, divisors(number))


total = 0
abundants = set()
nbsm = set()
nonsuum = set()

#generates a set of all the abundant numbers up to 28123
for num in range(12, 28124):
    if smdiv(num) > num: abundants.add(num)

#generate a set of all the numbers made by a sum of two abundant numbers up to 28123
for numa in abundants.copy():
    for numb in abundants.copy():
        suum = numa+numb
        if suum <= 28124: nbsm.add(suum)

#generates a set of all the nonsums
for i in range(1, 28124):
    if i not in nbsm:
        nonsuum.add(i)
print(reduce(operator.add, nonsuum))
