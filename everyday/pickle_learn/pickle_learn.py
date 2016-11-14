# -*- coding: utf-8 -*-
import cPickle
import numpy as np

'''
pickle.dump(obj, file[, protocol])

如果protocol没有设置, 则默认protocol = 0
如果protocal 值小于0(比如 -1), 或者 protocal=HIGHRST_PROTOCOL,  则使用最高协议的版本

pickle.load(file)


pickle.dumps(obj[, protocal])

'''


obj = {'a': 'b', 'c': 'd'}
obj2 = [0, 1, 1, 1, 0, 1]
fuck = np.random.random(10)
# print fuck


print cPickle.dumps(fuck)


f = open('obj.pkl', 'wb')
# cPickle.dump(obj, f, protocol=-1)
# cPickle.dump(obj2, f, protocol=-1)
cPickle.dump(fuck, f, protocol=-1)
f.close()

f = open('obj.pkl', 'rb')
x1 = cPickle.load(f)
f.close()


# print x1
