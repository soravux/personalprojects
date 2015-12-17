#! /usr/bin/env python3
biggest = 0
bestnum = 1
for number in range(1,1000000):
    chainlength = 1
    num = number
    while num != 1:
        chainlength += 1
        if num & 1:
            num = 3 * num + 1
        else: num = num // 2
    if chainlength > biggest:
        biggest = chainlength
        bestnum = number
print(bestnum)
