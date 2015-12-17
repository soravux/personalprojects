#! /usr/bin/env python

totaltot = 0

for number in range(1, 1001):
    tot = 0

    if number == 1000: tot = 11 # "one thousand"
    
    if number >= 100:
        tot += 7 # "hundred"
        if int(str(number)[-3]) in ('x', 0): tot -= 7
        if int(str(number)[-3]) in (1, 2, 6): tot += 3
        if int(str(number)[-3]) in (4, 5, 9): tot += 4
        if int(str(number)[-3]) in (3, 7, 8): tot += 5

        if number % 100 != 0: tot += 3 # "and"

    if number % 100 >= 20: 
        if int(str(number)[-2]) in (4, 5, 6): tot += 5
        if int(str(number)[-2]) in (2, 3, 8, 9): tot += 6
        if int(str(number)[-2]) in ('x', 7): tot += 7
        if int(str(number)[-2]) in ('x', 0): tot += 9


    if number % 100 >= 10 and number % 100 < 20: # 10, 11, ..., 19 
        if int(str(number)[-1]) in ('x', 0): tot += 3
        if int(str(number)[-1]) in (1, 2): tot += 6
        if int(str(number)[-1]) in (5, 6): tot += 7
        if int(str(number)[-1]) in (3, 4, 8, 9): tot += 8
        if int(str(number)[-1]) in ('x', 7): tot += 9

    elif number % 10 != 0:
        if int(str(number)[-1]) in (1, 2, 6): tot += 3
        if int(str(number)[-1]) in (4, 5, 9): tot += 4
        if int(str(number)[-1]) in (3, 7, 8): tot += 5
    totaltot += tot

print(totaltot)

