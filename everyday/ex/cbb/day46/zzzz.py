from collections import OrderedDict

'''
test the Ordered Diction
'''
evilpoints = OrderedDict([
                ('Orcs', 1),
                ('Men', 2),
                ('Wargs', 2),
                ('Goblins', 2),
                ('Uruk Hai', 3),
                ('Trolls', 5),
                ('Wizards', 10),
             ])

for i,j in evilpoints.iteritems():
    print i+':'+str(j)