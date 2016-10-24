f = open('catalysis.txt','r')
zz = open('zjw.txt','w')
for i in f.readlines():
    p = [k.rjust(9) for k in i.strip().split() if k]
    zz.write(''.join(p)+'\n')
f.close()
zz.close()
