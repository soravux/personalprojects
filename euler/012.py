#! /usr/bin/env python3
import math

num = 1 #number, used for generating the next trinum
trinum = 0 #the triangular number
divisors = []
while len(divisors) <= 250:
    trinum += num
    num += 1
    divisors = []
    sq = math.ceil(trinum ** 0.5)
    for divisor in range(1, sq+1):
        if trinum % divisor == 0: divisors.append(divisor)
print(trinum)

