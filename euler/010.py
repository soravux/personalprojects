#! /usr/bin/env python3
import operator
from functools import reduce
import math
primes = [2]
number = 3
top = 2000000
while number < top:
    divisible = False
    sq = math.ceil(number ** 0.5)
    for inst in primes:
        if inst > sq: break
        if number % inst == 0:
            divisible = True
            break
    if not divisible:primes.append(number)
    number += 1

print(reduce(operator.add, primes))
