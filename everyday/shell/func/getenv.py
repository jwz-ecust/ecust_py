from .constants import *


def getenv(args):
    if len(args):
        print os.getenv(args[0])
    return SHELL_STATUS_RUN
