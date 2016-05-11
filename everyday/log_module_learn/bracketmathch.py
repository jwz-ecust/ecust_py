# -*- coding: utf-8 -*-

left = {"(", "[","{"}
right = {")", "]","}"}


def match(expr):
    '''
    :param expr: 传过来的字符串
    :return: 返回是否是正确的
    '''
    stack = []
    for brackets in expr:
        if brackets in left:
            stack.append(brackets)
        elif brackets in right:
            if not stack or not 1 <= ord(brackets) - ord(stack[-1]) <= 2:
                return False
            stack.pop()
    return not stack


result = match("[(){()}]")
print result


result = match("{(]}")
print result
