# -*- coding -*-

__author__ = 'jwzhang'

from random import Random
import string

def codeGenerator(number, codelength = 8):
    print '**** Code Generator ****'
    with open('code.txt','w') as f:
        if number <= 0:
            return 'invalid number of codes'
        else:
            chars = string.digits+string.letters
            random = Random()
            for j in range(1,number+1):
                str = ''
                for i in range(1, codelength+1):
                    index = random.randint(1,len(chars))
                    str = str + chars[index-1]
                print str
                f.write(str+'\n')

print codeGenerator(200,4)