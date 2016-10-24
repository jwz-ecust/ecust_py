f = open('zzz.txt','r')
z = open('cbb.txt','w')
for i in f.readlines():
    if len(i.strip())>6:
        i = i.strip()
        i = ''.join([i for i in i.split() if i])
        z.write('\n'+i.strip()+"  ")
    else:
        z.write("    "+i.strip())
f.close()
z.close()