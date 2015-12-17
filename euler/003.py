#! /usr/bin/env python3

num = 600851475143

divisor = 2

while divisor <= num:
    if num % divisor == 0:
        num /= divisor
    else:
        divisor += 1
print(divisor)
