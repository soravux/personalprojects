#! /usr/bin/env python3

def prd():
    for a in range(1, 333):
        for b in range(a, 998):
            for c in range(b, 998):
                if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                    return a*b*c
print(prd())
