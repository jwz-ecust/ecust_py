import itertools


def check(a, b):
    for i in zip(a, b):
        if i in [('a', 'x'), ('c', 'x'), ('c', 'z')]:
            return
    else:
        return a, b


team_1 = ['a', 'b', 'c']
team_2 = ['x', 'y', 'z']



check_list = [('a', 'x'), ('c', 'x'), ('c', 'z')]
# for i in itertools.permutations(team_1, 3):
#     f = lambda a,b: len([True for j in zip(a, b) if j not in check_list])
#     if f(i, team_2) == 3:
#         print i, team_2

for i in itertools.permutations(team_1, 3):
    for j in zip(i, team_2):
        if j in check_list:
            break
    else:
        print i, team_2
