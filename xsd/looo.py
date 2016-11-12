# -*- coding: utf-8 -*-

import logging
from logging.config import fileConfig

fileConfig('./zzz.ini')
# create logger
logger = logging.getLogger('zjw')

# application Code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
