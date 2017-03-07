def read_file(fpath):
    BLOCK_SIZE = 1024
    with open(fpath, 'r') as f:
        block = f.read(BLOCK_SIZE)
        if len(block) > 40:
            yield block
        else:
            return


fpath = "/Users/zhangjiawei/Desktop/wechatrobot/mywechat.py"
for i in read_file(fpath):
    print i
    print len(i)
