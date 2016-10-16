class _const:
    class ConstError(TypeError):
        pass
    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            raise self.ConstError, "can not change const. %s" %name
        if not name.isupper():
            raise self.ConstCaseError, "%s is not all uppercase" %name
        self.__dict__[name] = value

import sys
sys.modules[__name__]=_const()
'''
Here, the sys.modules is a dict, which contains all modules start at the beginning of python start.
It is worth noting that the module in sys.modules dict may need to be import.
You can print the dict by "print sys.modules"
'''