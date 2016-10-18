from PIL import Image, ImageDraw, ImageFont
text = "zhangjiawei"
im = Image.open('zjw.bmp')

w, h = im.font_size    # get picture's size
font_size = h // 11     # set the font's size

draw = ImageDraw.Draw(im)       # set up a drawing
font = ImageFont.truetype("LucidaBrightItalic.ttf", font_size)
# choose font style and use the previous font size
print type(font)
# text_w, text_h = draw.textsize(text,font = font)      
# apply the font setting to the specific text
# draw.text((40,0),text,fill=(255,220,220),font=font)   
# draw the text at position, fill is color
# im.save('hehe.bmp')