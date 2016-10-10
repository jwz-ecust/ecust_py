# 函数参数
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print "{0}={1}".format(key,value)

d = dict(zjw='zhangjiawei',zyc='zhangyichen',cbb='chenbeibei')

greet_me(**d)


# 生成器
def generator():
    for i in range(10):
        yield  i

papa = generator()

for i in range(10):
    print papa.next()