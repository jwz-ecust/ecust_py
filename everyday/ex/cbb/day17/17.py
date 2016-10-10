#-*- coding: utf-8 -*-
'''
when creating class, you must add "()"
'''

import uuid

class generate_N_keys():
    def __init__(self):
        self.num = 0
        self.list = []

    def generate(self,Num):
        for i in range(Num):
            self.list.append(uuid.uuid1())

    def return_list(self):
        return self.list

test = generate_N_keys()
test.generate(200)
print test.list
