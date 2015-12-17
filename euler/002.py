#! /usr/bin/env python3

sum = 0
b, c = 1, 2
while c <= 4000000:
    sum += c
    b, c = b+2*c, 2*b+3*c

print(sum)
