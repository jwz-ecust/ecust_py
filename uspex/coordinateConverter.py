

def coordinateConverter(input, atom):
    # give input coordinate and atom dictionary
    lines = []
    for atom_type in atom.keys():
        for i in range(int(atom[atom_type])):
            tt = filter_blank(input[i].strip().split())
            t = atom_type.rjust(2) + ' ' * 11 + '     '.join(tt) + '\n'
            lines.append(t)
    return lines


def filter_blank(line):
    '''
    filter blank in  a given list
    '''
    return [_ for _ in line if _]


atom = {'Ni': '6', 'P': '12'}
input = [
    '0.613649     0.503403     0.611686',
    '0.377635     0.498432     0.615444',
    '0.495119     0.378911     0.401412',
    '0.504112     0.612433     0.405174',
    '0.998609     0.995823     0.002261',
    '0.001428     0.004232     0.501744',
    '0.997421     0.497384     0.342258',
    '0.497667     0.001971     0.652714',
    '0.304534     0.004326     0.966089',
    '0.697818     0.994647     0.958166',
    '0.996191     0.699323     0.037818',
    '0.996970     0.300392     0.028471',
    '0.746193     0.495953     0.456521',
    '0.245700     0.504996     0.454939',
    '0.498529     0.248652     0.542184',
    '0.498857     0.753176     0.550156',
    '0.000887     0.502307     0.050088',
    '0.495195     0.999225     0.962897',
]


print coordinateConverter(input, atom)
