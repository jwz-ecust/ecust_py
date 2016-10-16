import re
def readincar(file):  # the path of INCAR file
    with open(file,'r') as f:
        equations = []
        parameters={}
        contnets = [i for i in f.readlines() if i!='\n']
        for index in contnets:
            index = re.sub(' ','',index)
            if not (index.startswith('%') or index.startswith('!')):
                if "<->" in index:
                    equations.append(index.strip())
                else:
                    c1,c2=index.split('=')
                    parameters[c1]=c2.split(';')[0]
    return equations,parameters


print readincar('INCAR')