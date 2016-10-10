from collections import OrderedDict

goodpoints = OrderedDict([
                ('Hobbits', 1),
                ('Men', 2),
                ('Elves', 3),
                ('Dwarves', 3),
                ('Eagles', 4),
                ('Wizards', 10),
             ])
evilpoints = OrderedDict([
                ('Orcs', 1),
                ('Men', 2),
                ('Wargs', 2),
                ('Goblins', 2),
                ('Uruk Hai', 3),
                ('Trolls', 5),
                ('Wizards', 10),
             ])

def goodVsEvil(good, evil):
    gp = sum(x * int(y) for x, y in zip(goodpoints.values(), good.split()))
    ep = sum(x * int(y) for x, y in zip(evilpoints.values(), evil.split()))
    
    if gp > ep:
        return 'Battle Result: Good triumphs over Evil'
    elif gp < ep:
        return 'Battle Result: Evil eradicates all trace of Good'
    else:
        return 'Battle Result: No victor on this battle field'