import numpy as np
import os
from PIL import Image


class pic2cnn:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    IMAGE_HEIGHT = 114
    IMAGE_WIDTH = 450
    char_set = alphabet + ['_']  # 如果验证码长度小于6, '_'用来补齐
    char_dic = {}
    for i, j in enumerate(char_set):
        char_dic[j] = float(i)
    MAX_CAPTCHA = 6

    def text2vec(self, text):
        text_len = len(text)
        if text_len > self.MAX_CAPTCHA:
            raise ValueError('验证码最长6个字符')
        if text_len < self.MAX_CAPTCHA:
            text = text + (self.MAX_CAPTCHA - text_len) * "_"

        vector = np.zeros(self.MAX_CAPTCHA * len(self.char_set), dtype=np.int)

        def char2pos(c):
            return self.char_dic[c]

        for i, c in enumerate(text):
            vector[i * len(self.char_set) + int(char2pos(c))] = 1
        return vector

    def vec2text(self, vector):

        def find_key(i):
            for _ in self.char_dic.keys():
                if self.char_dic[_] == i:
                    return _

        vector = vector.reshape((6, -1))
        maxindex = vector.argmax(axis=1)
        return "".join([find_key(i) for i in maxindex])


    def gendata(self):
        cwd = "/Users/zhangjiawei/Downloads/captcha2000"
        picfiles = os.listdir(cwd)
        num = len(picfiles)
        x = np.zeros((num, self.IMAGE_HEIGHT, self.IMAGE_WIDTH))
        y = np.zeros((num, self.MAX_CAPTCHA * len(self.char_set)), dtype=np.int)

        for i, p in enumerate(picfiles):
            pic = os.path.join(cwd, p)
            img = Image.open(pic)
            img = np.array(img, dtype=np.int)
            x[i] = img

            v = self.text2vec(p.split(".")[0])
            y[i] = v
        return x, y


    def generatebatch(self, x, y, batch):
        num = x.shape[0]
        choose = np.random.choice(range(num), batch)
        x = x[choose, :]
        y = y[choose, :]
        x = x.reshape(batch, -1)
        return x, y



#
# zjw = pic2cnn()
# x, y = zjw.gendata()
#
# p = zjw.generatebatch(x, y, 50)
# p2 = zjw.generatebatch(x, y, 50)
# print(p == p2)
#
#
#
#
















