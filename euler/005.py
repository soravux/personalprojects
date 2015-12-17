#! /usr/bin/env python3

number = 20

def small(num):
    number = num
    while True:
        for i in reversed(range(num)):
            if number % i == 0:
                if i == 1:
                    return number
            else:
                break
        number += num

print(small(number))
