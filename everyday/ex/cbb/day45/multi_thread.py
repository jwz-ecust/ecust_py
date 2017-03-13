# -*- coding: utf-8 -*-
import threading
import logging


class MyThread(threading.Thread):
    def __init__(self, number, logger):
        threading.Thread.__init__(self)
        self.number = number
        self.logger = logger

    def run(self):
        '''
        运行线程
        '''
        logger.debug('Calling doubler')
        double(self.number, self.logger)


def get_logger():
    logger = logging.getLogger("threading_example")
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler("threading.log")
    fmt = '%(asctime)s-%(threadName)s-%(levelname)s-%(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger


def double(number, logger):
    '''
    可以被线程使用的一个函数
    '''
    logger.debug('double function executing')
    result = number * 2
    logger.debug('doubler function ended with: {}'.format(result))


if __name__ == '__main__':
    logger = get_logger()
    thread_names = ['Mike', 'Dick', 'Ass', 'Hole', 'Harden', 'Curry']
    for i in range(6):
        thread = MyThread(i, logger)
        thread.setName(thread_names[i])
        thread.start()
