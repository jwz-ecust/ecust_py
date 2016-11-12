# coding: utf-8

import logging


# logging.basicConfig(filename='zjw.log', level=logging.INFO)
#
# logging.debug('debug message')
# logging.info('info message')
# logging.warn('warn message')
# logging.error('error message')
# logging.critical('critical message')


'''
==================================================================
'''
#  more complete
'''
    Logger 即记录器，Logger提供了日志相关功能的调用接口。
    Handler 即处理器，将（记录器产生的）日志记录发送至合适的目的地。
    Filter 即过滤器，提供了更好的粒度控制，它可以决定输出哪些日志记录。
    Formatter 即格式化器，指明了最终输出中日志记录的格式。
'''

logger = logging.getLogger("zjw")

z1 = logging.StreamHandler()
z2 = logging.FileHandler('logging.log')
z1.setLevel(logging.DEBUG)
z2.setLevel(logging.INFO)

# create formater
formatter = logging.Formatter(
    "%(asctime)s-%(name)s - %(levelname)s - %(message)s")

# add formatter to z
z1.setFormatter(formatter)
z2.setFormatter(formatter)

# add Handler to logger
# The final log level is the higher one betwen the default and the one in
# handler
logger.addHandler(z1)
logger.addHandler(z2)


# add message to logger
logger.debug('dedug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
