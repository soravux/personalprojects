#! /usr/bin/env python

daycount = 2 
sundaycount = 0

def isSunday():
    global daycount
    global sundaycount
    if daycount % 7 == 0:
        sundaycount += 1

# September, April, June, November = 30 days
# January, March, May, July, August, October, December = 31 days
# February = 28/29 days

year = 1901
month = 1 

while year < 2001:
    month = 1
    while month < 13:
        if month in (1, 3, 5, 7, 8, 10, 12): # 31 days
            isSunday()
            daycount += 31

        elif month in (4, 6, 9, 11): # 30 days
            isSunday()
            daycount += 30

        elif month in ('x', 2): # february
            isSunday()
            daycount += 28
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0: daycount += 1
                else: daycount += 1
        
        month += 1


    year += 1

print(sundaycount)
