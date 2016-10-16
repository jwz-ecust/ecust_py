from collections import namedtuple

def ExtractCoefficient(equations):
    length = len(equations)
    reaction_tuple = []
    for index in range(length):
        equation = equations[index]
        reaction_name = 'reaction'+str(index)
        reaction_name = namedtuple(reaction_name,['reactants','prodects','intermediates'])
        react,produc = equation.split('<->')
        for i

    #
    #     react = [i.strip() for i in react.split('+')]
    #     produc = [j.strip() for j in produc.split('+')]
    #     reaction_name.forward = react
    #     reaction_name.reverse = produc
    #     reaction_tuple.append(reaction_name)
    # return reaction_tuple

equations=[
    'NO + #1 <-> ON#1',
    'ON#1 + O#2 <-> ONO#2 + #1',
    'ONO#2 <-> NO2 + #2',
    'O2 + #2 <-> O2#2',
    'O2#2 + ON#1 <-> N#2 + #1',
    'N#2 + #1 <-> NO2#1 + O#2',
    'NO2#1 <-> NO2 + #1'
]


ExtractCoefficient(equations)