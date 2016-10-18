#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
this script is used to generate identifying picture, including four characters.
'''
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

__author__ = 'zhangjiawei'


# generate the random code
def rndChar():
    return chr(random.randint(65, 90))


def rndColor(type):
    if type == 1:
        return (random.randint(0, 125), random.randint(0, 125),
                random.randint(0, 125))
    elif type == 2:
        return (random.randint(126, 255), random.randint(126, 255),
                random.randint(126, 25))


fontSize = 250
width = int(fontSize * 1.2 * 4)
height = int(fontSize * 1.2)

# create the image instance
image = Image.new('RGB', (width, height), (255, 255, 255))

# create the font instance
font = ImageFont.truetype("Skia.ttf", 200)

# starting of draw
draw = ImageDraw.Draw(image)
# fill the whole picture
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor(1)


for t in range(100):
    draw.text((t * height + fontSize * 0.2, fontSize * 0.2), rndChar(),
        font=font, fill=rndColor(2))



if __name__ == '__main__':
    image.show()
