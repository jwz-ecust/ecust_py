class zjw(object):
    def __new__(cls, name, age):
        return super(zjw, cls).__new__(cls, name, age)

    # def __init__(self,name,age):
    #     self.name = name
    #     self.age = age
    # def __str__(self):
    #     return "{}      {}".format(self.name, self.age)


a1 = zjw()
print a1
