#! /usr/bin/env python

import math
import operator
from functools import reduce

print(reduce(operator.add, (int(i) for i in str(math.factorial(100)))))
