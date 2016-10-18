# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

'''
This is a script to draw any character you want to a photo
in which includes a class
class-generate: Image_unread_message
                属性: open, setFont, draw_text
                      fnt, im
'''


class Image_unread_message:
    def open(self, path):
        self.im = Image.open(path)
        return True

    def __init__(self):
        self.fnt = None
        self.im = None

    def setFont(self, font_path, size):
        self.fnt = ImageFont.truetype(font_path, size)
        return True

    def draw_text(self, position, str, color, fnt):
        draw = ImageDraw.Draw(self.im)
        draw.text(position, str, fill=color, font=fnt)
        self.im.show()
        self.im.save(str + 'num' + '.jpg')
        return True


test = Image_unread_message()
test.open('test.png')
test.setFont('ahronbd.ttf', 50)
test.draw_text((0, 0), 'ZJW', (255, 0, 0), test.fnt)
