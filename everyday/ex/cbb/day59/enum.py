from collections import namedtuple

def enum(*posarg,**keysarg):
    return type("Enum",(object,),dict(zip(posarg,xrange(len(posarg))),**keysarg))

Seasons = enum("spring","summer","autumn",winter=1)

print type(Seasons)


ss = namedtuple("ss",['Spring','Summer','Autumn','Winter'])._make([0,2,1,2])
zjw = ss._replace(Spring=9)
print zjw