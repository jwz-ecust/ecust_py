# -*- coding: utf-8 -*-
def countBits(n):
    bit_num = bin(n)[2:]
    return sum([int(i) for i in str(bit_num)])

def ccc(n):
    return bin(n).count('1')

def ccc_2(n):
    total = 0
    while n>0:
        total += n%2    # 如果n被2整除，则没有余数，可以向右移一位；否则total+1，再移一位
        n >>= 1
    return total

print countBits(0)
print countBits(4)
print countBits(7)
print countBits(10)