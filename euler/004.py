#! /usr/bin/env python3
bottom = 100
top = 999
step = 1
number = 0 

for a in range(bottom, top):
    for b in range(bottom, top):
        if a*b > number and str(a*b) == str(a*b)[::-1]:
            number = a*b

print(number)
