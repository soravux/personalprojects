#! /usr/bin/env python3

top = 100
naturals = range(top+1)
sqnats = [i ** 2 for i in naturals]
sumsquare = sum(sqnats)
squaresum = (sum(range(top+1)) ** 2)

print(squaresum - sumsquare)
