from collections import namedtuple,Counter

def creat_poscar(filepath):
    # first, extract data(postion,atom type and number, and vector)
    j = 0
    atom_list = []
    vector = {}
    with open(filepath,'r') as file:
        content = file.readlines()
        for i in content:
            if i.find('XYZ')!=-1:
                tt=i.strip().split(' ')
                for i in tt:
                    if i.find('XYZ')!=-1:
                        xyz = i.split('=')[1].strip('"').split(',')
                    elif i.find('Components')!=-1:
                        component = i.split('"')[-2]
                p = 'postion'+component+str(j)
                p = namedtuple(p,['x','y','z','name'])
                p.x,p.y,p.z=xyz[0][:15],xyz[1][:15],xyz[2][:15]
                p.name =component
                atom_list.append(p)
                j +=1
            elif i.find('SpaceGroup')!=-1:
                ttt = i.strip().split(' ')
                for j in ttt:
                    if j.find('Vector')!=-1:
                        temp = j.split('=')
                        vector[temp[0]]=temp[1].strip('"').split(',')
    # write data into POSCAR file
    atom_name = [i.name for i in atom_list]
    atom_type = set(atom_name)
    cc = Counter(atom_name)
    with open('POSCAR','w') as pp:
        pp.write('poscar_create_by_python\n')
        pp.write('1.000000'+'\n')
        for k in sorted(vector.keys()):
            pp.write('    '+'    '.join(Vector[k])+'\n')
        pp.write('    ')
        for i in atom_type:
            pp.write(i+'    ')
        pp.write('\n')
        pp.write('    ')
        for i in atom_type:
            pp.write(str(cc[i])+'    ')
        pp.write('\n')
        con = []
        for i in atom_list:
            zjw = '  '.join([i.x,i.y,i.z])
            con.append(' '*4+zjw+'\n')
        pp.writelines(con)

creat_poscar('./zjw.xsd')