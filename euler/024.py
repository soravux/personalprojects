#! /usr/bin/env python
import math
import operator
from functools import reduce

digits = [str(x) for x in range(10)]
vchoice = 1000000-1
nb = []

for a in reversed(range(len(digits))):
        nb.append(digits.pop(vchoice // math.factorial(a)))
        vchoice %= math.factorial(a)

print(reduce(operator.add, nb))
