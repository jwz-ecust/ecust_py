class ppp(object):
    _attrs = ['name', 'age', 'height', "school", "lang", "wife"]

    def __init__(self):
        pass

    def __getattribute__(self, *attr):
        return object.__getattribute__(self, *attr)

    def __setattr__(self, *attr, **value):
        object.__setattr__(self, *attr, **value)

    # def __repr__(self):
    #     return "zhangjiawei"

    def __str__(self):
        return "zhangjjiawei"

zjw = ppp()

attr = ['name', 'age', 'height', "school", "lang", "wife"]
value = {
    'name' : 'zjw',
    'age': 26,
    'height': 173,
    "school": 'ecust',
    "lang": 'python',
    "wife": 'cbb'
}
zjw.name = 'cbb'
print zjw.name
print zjw
