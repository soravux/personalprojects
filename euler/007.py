#! /usr/bin/env python3

primes = []
number = 2

while len(primes) < 10001:
    divisible = False
    for i in primes:
        if number % i == 0:
            divisible = True
            break
    if not divisible:
        primes.append(number)
    number += 1

print(primes[-1])
