def zjw():
    a = iter([1,2,3])
    for i in range(10):
        print next(a,2)

'''
运行结果:
1
2
3
2
2
2
2
2
2
2
next(iteration_object,num)
iteration_object:迭代对象;
num: 默认值(如果迭代到没有了,就是这个值)
'''
