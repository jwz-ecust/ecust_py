for i in range(1, 10):
    res = []
    for j in range(1, i + 1):
        l = "%dx%d=%d" % (i, j, i * j)
        res.append(l)
    print ' '.join(res)
