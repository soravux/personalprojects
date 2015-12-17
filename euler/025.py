#! /usr/bin/env python
a = 1
b = 1
term = 2
numdigit = 1000
while len(str(b)) < numdigit:
    a, b = b, a+b
    term += 1
print(term)

