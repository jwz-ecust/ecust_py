import re
def is_valid_IP_1(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit() or x.startswith('0'):
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True

def is_valid_IP_2(s):
    a = s.split('.')
    passed = 0
    for i in a:
        if i.isdigit():
            if i[0] != '0':
                if 0<int(i)<=255:
                    passed+=1
    return passed==4

def is_valid_IP_3(s):
    return re.match('\.'.join(['(\d|1?\d\d|2[0-4]\d|25[0-5])']*4)+'$',s) is not None

def is_valid_IP_5(s):
    return s.count('.') == 3 and all(o.isdigit() and 0< int(o) <= 255 and str(int(o))==o for o in s.split('.'))
