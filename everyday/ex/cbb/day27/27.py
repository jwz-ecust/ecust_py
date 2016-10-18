# -*- coding: utf-8 -*-

import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def random_string(y):
    '''
    生成指定长度的随机字符串
    '''
    return ''.join(random.choice(string.letters) for x in range(y))


def create_verifi_image(strs, **d):
    width, height = d['size']
    img = Image.new(d['mode'], d['size'], d['bg_color'])
    draw = ImageDraw.Draw(img)

    if d['draw_lines']:
        line_num = random.randint(*d['n_line'])
        for i in range(line_num):
            begin = (random.randint(0, d['size'][0]), random.randint(
                0, d['size'][1]))
            end = (random.randint(0, d['size'][0]), random.randint(
                0, d['size'][1]))
            draw.line([begin, end], fill=(0, 0, 0))

    if d['draw_points']:
        chance = min(100, max(0, int(d['point_chance'])))
        for w in range(width):
            for h in range(height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    draw.point((w, h), fill=(0, 0, 0))

    font = ImageFont.truetype(d['font_type'], d['font_size'])
    font_width, font_height = font.getsize(strs)
    print font_width, font_height
    draw.text((0, 0), strs, font=font, fill=d['fg_color'])
    params = [
        1 - float(random.randint(1, 2)) / 100,
        0, 0, 0,
        1 - float(random.randint(1, 10)) / 100,
        float(random.randint(1, 2)) / 500,
        0.001, float(random.randint(1, 2)) / 500]
    img = img.transform(d['size'], Image.PERSPECTIVE, params)
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return img


if __name__ == '__main__':
    parameters = {
        'size': (600, 300),
        'mode': 'RGB',
        'bg_color': (255, 255, 255),
        'fg_color': (0, 0, 255),
        'font_size': 100,
        'font_type': 'ahronbd.ttf',
        'draw_lines': True,
        'n_line': (1, 2),
        'draw_points': True,
        'point_chance': 2
    }
    strs = random_string(4)
    # print parameters['size']
    code_img = create_verifi_image(strs, **parameters)
    code_img.show()
    code_img.save('validate.jpg')
