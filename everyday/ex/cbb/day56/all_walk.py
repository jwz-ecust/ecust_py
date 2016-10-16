import os
import xlwt

def extract_info(path):
    with open(path+'/'+'OSZICAR','r') as oszicar:
        content_1 = oszicar.readlines()
        energy_list = [i1 for i1 in content_1 if 'F' in i1][-1].strip().split()
        step = int(energy_list[0])
        gE = float(energy_list[2])
    with open(path+'/'+'OUTCAR','r') as outcar:
        content_2 = outcar.readlines()
        gF = float([i2 for i2 in content_2 if 'RMS' in i2][-1].strip().split()[4])
        if 'fort.188' in os.listdir(path):
            dis = float([i3 for i3 in content_2 if 'dis' in i3][-1].strip().split()[3])
        else:
            dis = 'not TS'
    path = '/'.join(path.split('/')[4:])
    return path,gF,gE,step,dis

direct_path = os.getcwd()
excel_sheet_name = direct_path.split('/')[-1]
dir_list = os.walk(direct_path)
data = xlwt.Workbook()
table = data.add_sheet(excel_sheet_name)
table.write(0,0,'Path')
table.write(0,1,'Force')
table.write(0,2,'Energy')
table.write(0,3,'Steps')
table.write(0,4,'TS distance')

i = 0
for sub_index in dir_list:
    work_dir = sub_index[0]
    content_list = sub_index[2]
    i+=1
    if 'OUTCAR' in content_list and 'OSZICAR' in content_list:
        info = extract_info(work_dir)
        for j in range(len(info)):
            table.write(i,j,info[j])
data.save(direct_path+'.xls')
