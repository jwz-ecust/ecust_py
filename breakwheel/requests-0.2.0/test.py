class zjw(object):
    def __init__(self, start, step, data):
        self.data = data
        self.value = start - step
        self.step = step
        self.stop = len(data)

    def __getitem__(self, i):
        print "fuck!"
        return self.data[i]

    def __iter__(self):
        print "holy shit"
        return self
    def next(self):
        if self.value >= self.stop -1:
            raise StopIteration
        self.value += self.step
        return self.data[self.value]
    def __del__(self):
        print "goodbly", self


# p = zjw(0, 2, "zhangjiawei")
# for i in p:
#     print i
#



class Employee(object):
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def giveRaise(self, percent):
        self.salary = self.salary + (self.salary * percent)

    def work(self):
        print self.name, " does stuff"

    def __repr__(self):
        return "<Employee: name=%s, salary=%s>" %(self.name, self.salary)


class Chef(Employee):
    def __init__(self, name):
        super(Chef, self).__init__(name, 5000)

    def work(self):
        # super(Chef, self).work()
        print self.name, " make food"


class zz(Chef):
    def __init__(self, name):
        super(zz, self).__init__(name)

    def work(self):
        super(zz, self).work()


#
# pp = Chef('paul')
# pp.work()
# pp.giveRaise(0.5)
# print pp.salary


zw = zz('fla')
zw.work()
