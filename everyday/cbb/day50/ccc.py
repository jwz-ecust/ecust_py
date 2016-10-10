def rewrite(file):
    with open(file,'r') as f:
        res = []
        for line in f.readlines():
            print line
            if len(line)>1 and (not line.startswith('#')):
                res.append(line.strip()+'\n')
    res.sort()
    print res
    with open('cbb.txt','w') as n:
        n.writelines(res)

rewrite('zjw.txt')
