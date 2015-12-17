#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       untitled.py
#
#       Copyright 2011 znuxor <znuxor@gmail.com>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#
#
import sys

def mapParser(mapName):
    # This function reads the appropriate map file and parses it in (y,x)
    # lists inside lists.
    mapRawData = open("maps/"+mapName, "r").read()
    mapSplitData = mapRawData.split("\n")
    for line in mapSplitData:
        line = list(line)
    return mapSplitData

def mapPrinter(maplist):
    # This function prints the map to the terminal. It joins line elements
    # and print each lines separately.
    for line in maplist:
        print "".join(line)

    return 0

def main():
    play = 1
    nextmap = "tutorial1.txt"
    currentMap = mapParser(nextmap)
    while play == 1:
        keystroke = sys.stdin.read(2)
        mapPrinter(currentMap)

        print "Keystroke is " + keystroke
    return 0

if __name__ == '__main__':
    main()

