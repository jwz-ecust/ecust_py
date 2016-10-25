f = open('catalysis.txt','r')
zz = open('zjw.txt','w')
for i in f.readlines():
    i = ''.join([i.rjust(10) for i in i.split()][1:])
    zz.write(i+'\n')

f.close()
zz.close()