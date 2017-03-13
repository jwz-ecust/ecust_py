from .constants import *


def cd(args):
    if len(args) > 0:
        os.chdir(args)
    else:
        os.chdir(os.getenv('HOME'))
    return SHELL_STATUS_RUN
