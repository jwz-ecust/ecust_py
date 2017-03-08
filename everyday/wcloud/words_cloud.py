# -*- coding: utf-8 -*-
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba


# FONT_PATH = os.environ.get("FONT_PATH", os.path.join(os.path.dirname(__file__), "simhei.ttf"))
# print FONT_PATH



text_from_file_with_apath = open("/Users/zhangjiawei/Code/zjw/everyday/wcloud/wsbrook.txt").read()

wordlist = jieba.cut(text_from_file_with_apath, cut_all=True)
wl_space_split = " ".join(wordlist)

my_wordcloud = WordCloud().generate(wl_space_split)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
