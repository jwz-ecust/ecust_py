# -*- coding: utf-8 -*-

def filter_word(input_word):
    input_word = input_word.split()
    filter_word_list = []
    with open('./filter_word.txt') as f:
        for content in f:
            filter_word_list.append(content.strip('\n'))
    return filter_word_list

if __name__ == '__main__':
    input_words = input('Input some words:\n')
    input_words_list = input_words.split()
    filter_word_list = filter_word(input_words)

    word_string = ''
    for word in input_words_list:
        if word in filter_word_list:
            word = '*'*len(word)
        word_string += word + ' '
    print word_string
    print filter_word_list