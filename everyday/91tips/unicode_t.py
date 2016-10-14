# coding=utf-8
s = "张佳伟"
print isinstance(s, unicode)
print s.decode("utf-8").encode("gbk")