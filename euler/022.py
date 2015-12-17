#! /usr/bin/env python

f = open('names.txt', 'r')
names = f.readlines()[0].split('","')
names[0] = names[0][1:]
names[-1] = names[-1][:-1]
names.sort()

megatot = 0
for i in range(len(names)):
    name = names[i]
    tot = 0
    for letter in name:
        value = ord(letter)-64
        tot += value
    tot *= i+1
    megatot += tot

print(megatot)
