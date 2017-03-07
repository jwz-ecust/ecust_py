path = "/Users/zhangjiawei/Code/zjw/xsd/catalysis/NiP/data_mining/data.txt"
with open(path) as zjw:
    content = zjw.readlines()
    total = 110
    fuck = open('./ml_data.txt', 'w')
    for i in range(total):
        sub_cont = content[i * 15:i * 15 + 11]
        data = []
        ads = sub_cont[1].split(':')[-1].strip()
        line = ''
        for tt in sub_cont[2:]:
            tt = tt.rstrip().split('\t')
            if tt[0] == 'P':
                line = line + '0' + ' ' + tt[2] + \
                    ' ' + tt[-2] + ' ' + tt[-1] + ' '
            else:
                line = line + '1' + ' ' + tt[2] + \
                    ' ' + tt[-2] + ' ' + tt[-1] + ' '
        line = line + ads
        fuck.write(line + '\n')
    fuck.close()
