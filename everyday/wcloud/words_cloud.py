# -*- coding: utf-8 -*-
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import jieba
import numpy as np
from PIL import Image


text_from_file_with_apath = open("/Users/zhangjiawei/Code/zjw/everyday/wcloud/wsbrook.txt").read()
mask = np.array(Image.open("/Users/zhangjiawei/Code/zjw/everyday/wcloud/zjw.jpeg"))

stopwords = set(STOPWORDS)
stopwords.add("said")

# wordlist = jieba.cut(text_from_file_with_apath, cut_all=True)
# wl_space_split = " ".join(wordlist)

my_wordcloud = WordCloud(background_color='white', mask=mask, max_words=200).generate(text_from_file_with_apath)

# store to file
my_wordcloud.to_file("./cbb.jpg")

plt.imshow(my_wordcloud)
plt.axis("off")
plt.axis("off")
plt.show()
