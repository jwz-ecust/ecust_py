# -*- coding: utf-8 -*-

try:
    print('I am sure no exception is going to occur!')
    print 1/0
except Exception as e:
    print('exception')
    print e
else:
    # 这里的代码只会在try语句里没有触发异常时运行,
    # 但是这里的异常将 *不会* 被捕获
    print('This would only run if no exception occurs. And an error here would NOT be caught.')
finally:
    print('This would be printed in every case.')
