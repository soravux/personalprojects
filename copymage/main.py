#!/usr/bin/env python3
from PIL import Image
from random import randint
import os.path
import sys

def imgdiff(pixone, pixtwo, size):
    total = 0
    for i in range(size[0]):
        for j in range(size[1]):
            for k in range(3):
                total += abs(pixone[i, j][k] - pixtwo[i, j][k])
    return total

filebase = sys.argv[1]
otherfile = filebase[:-4]+"gen"+filebase[-4:]
nbrajouts = 1 

baseimg = Image.open(filebase)

if os.path.isfile(otherfile):
    imgone = Image.open(otherfile)
    imgtwo = Image.open(otherfile)
    if imgone.size != baseimg.size:
        imgone = Image.new( 'RGB', baseimg.size, "black")
        imgtwo = Image.new( 'RGB', baseimg.size, "black")
else:
    imgone = Image.new( 'RGB', baseimg.size, "black")
    imgtwo = Image.new( 'RGB', baseimg.size, "black")

pixbase = baseimg.load()
pixone = imgone.load()
pixtwo = imgtwo.load()
saveone = Image.new( 'RGB', baseimg.size, "black")
savetwo = Image.new( 'RGB', baseimg.size, "black")
iteration = 0

lastbestscore = imgdiff(pixbase, pixone, baseimg.size)
bumpnumber = 0
lastbump = bumpnumber
notperfect = True

while notperfect:
    saveone.paste(imgone)
    savetwo.paste(imgtwo)
    lastbump = bumpnumber

    for iter in range(nbrajouts):
        loc = (randint(0, baseimg.size[0]-1), randint(0, baseimg.size[1]-1))

        newpixone = list(pixone[loc])
        newpixtwo = list(pixtwo[loc])

        k = randint(0, 2)
        
        newpixone[k] = randint(0, 255)
        newpixtwo[k] = randint(0, 255)

        pixone[loc] = tuple(newpixone)
        pixtwo[loc] = tuple(newpixtwo)

    scoreone = imgdiff(pixbase, pixone, baseimg.size)
    scoretwo = imgdiff(pixbase, pixtwo, baseimg.size)

    if scoreone <= scoretwo and scoreone < lastbestscore:
        imgtwo.paste(imgone)
        imgone.save(otherfile)
        bumpnumber += 1
        lastbestscore = scoreone

    elif scoretwo < lastbestscore:
        imgone.paste(imgtwo)
        imgtwo.save(otherfile)
        bumpnumber += 1
        lastbestscore = scoretwo

    else:
        imgone.paste(saveone)
        imgtwo.paste(savetwo)

    if lastbestscore == 0:
        notperfect = False

    iteration += 1
    if lastbump != bumpnumber:
        print("iteration: " + str(iteration) + ", lastbestscore: " + str(lastbestscore) + ", bumpnumber: " + str(bumpnumber))

print("Done!")
