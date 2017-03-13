class A(object):

    def __init__(self):
        print "A"
        pass


class B(A):

    def __init__(self):
        super(B, self).__init__
        print "B"


class C(B, A):

    def __init__(self):
        super(C, self).__init__
        print "C"


class Person(object):
    name = ""
    sex = ""

    def __init__(self, name, sex="U"):
        print "person"
        self.name = name
        self.sex = sex


class Consumer(object):

    def __init__(self):
        print "cosumer"


# class stu(Person, Consumer):
class stu(Consumer, Person):

    def __init__(self, score, name):
        # super(stu, self).__init__(name, sex="F")
        # Consumer.__init__
        super(stu, self).__init__()
        Person.__init__(self, name, sex="fuck")
        self.score = score


s1 = stu(100, 'zjw')
print s1.name, s1.score, s1.sex


class Base(object):

    def __init__(self):
        print "base created"


class childA(Base):

    def __init__(self):
        Base.__init__(self)


class childB(Base):

    def __init__(self):
        super(childB, self).__init__()


print childA(), childB()
