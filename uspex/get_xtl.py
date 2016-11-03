import numpy as np


def get_xtl(gatheredposcars_path):
    with open(gatheredposcars_path) as gp:
        content = gp.readlines()
        num_of_pos = content.count('1.0000\n')
        num_of_each = len(content) / num_of_pos
        for i in range(num_of_pos):
            lattice_info = content[i * num_of_each + 2:i * num_of_each + 5]
            lattice = latConverter(lattice_info)
            atom_type = ['Ni', 'P']
            atom_number = content[i * num_of_each + 5].strip().split('   ')
            # generate atom dictionary
            atom = dict(zip(atom_type, atom_number))
            atom_coordinates = content[
                i * num_of_each + 7: (i + 1) * num_of_each - 1]
            lattice_line = '     '.join(
                ['{0:6f}'.format(i) for i in lattice])
            print lattice_line


def filter_blank(line):
    '''
    filter blank in  a given list
    '''
    return [_ for _ in line if _]


def latConverter(input):
    output = np.zeros(6)
    x = np.array(filter_blank(input[0].strip().split(' ')), dtype=np.float)
    y = np.array(filter_blank(input[1].strip().split(' ')), dtype=np.float)
    z = np.array(filter_blank(input[2].strip().split(' ')), dtype=np.float)
    output[0] = np.sqrt(sum(np.square(x)))
    output[1] = np.sqrt(sum(np.square(y)))
    output[2] = np.sqrt(sum(np.square(z)))
    output[3] = np.arccos(x.dot(y) / (output[0] * output[1])) * 180.0 / np.pi
    output[4] = np.arccos(x.dot(z) / (output[0] * output[2])) * 180.0 / np.pi
    output[5] = np.arccos(y.dot(z) / (output[1] * output[2])) * 180.0 / np.pi
    return output


def coordinateConverter(input, atom):
    # give input coordinate and atom dictionary
    pass


path = '/Users/zhangjiawei/Code/zjw/uspex/gatheredPOSCARS'
get_xtl(path)
