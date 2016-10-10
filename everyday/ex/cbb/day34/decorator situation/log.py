# -*- coding: utf-8 -*-
from functools import wraps

def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args,**kwargs):
            log_string = func.__name__ + ' was called'
            print log_string
            # 现在将日志写入指定的logfile
            with open(logfile,'a') as opened_file:
                opened_file.write(logfile+'\n')
            return func(*args,**kwargs)
        return wrapped_function
    return  logging_decorator


@logit()
def zjw():
    pass

zjw()


@logit(logfile='cbb.log')
def zzz():
    pass
zzz()