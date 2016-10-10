from functools import wraps

class logit(object):
    def __init__(self,logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args,**kwargs):
            log_string = func.__name__ + " was called"
            print log_string
            with open(self.logfile,'a') as opened_file:
                opened_file.write(log_string+'\n')
            self.notify()
            return func(*args,**kwargs)
        return wrapped_function

    def notify(self):
        pass

class email_logit(logit):
    '''
    一个logit的实现版本，可以在函数调用时发送email给管理员
    '''
    def __init__(self,email='admin@myproject.com',*args,**kwargs):
        self.email = email
        super(logit,self).__init__(*args,**kwargs)
    def notify(self):
        #发送一封email到self.emal
        #这里就不做实现
        pass
        # 从现在起， @email_logit 将会和 @logit 产生同样的效果，但是在打日志的基础上，还会多发一封邮件给管理员