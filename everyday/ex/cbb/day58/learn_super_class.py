# without super
class FooParent(object):
    def __init__(self):
        self.parent = "I am the parent"
        print 'Parent'

    def bar(self,message):
        print message, 'from Parent'

class FooChild(FooParent):
    def __init__(self):
        FooParent.__init__(self)
        print 'Child'

    def bar(self,message):
        FooParent.bar(self,message)
        print 'Child bar function.'
        print self.parent

if __name__ == '__main__':
    foochild = FooChild()  #initing the class
    foochild.bar("hello zhangjiawei")

'''
The result:
Parent
Child
hello zhangjiawei from Parent
Child bar function.
I am the parent
'''

#########################################################
# with super
class Parent(object):
    def __init__(self):
        self.parent = "I am the parent"
        print 'Parent'

    def bar(self,message):
        print message, 'from Parent'

class Child(Parent):
    def __init__(self):
        super(Child,self).__init__()
        print "Child"

    def bar(self,message):
        super(Child,self).bar(message)
        print "Child bar function"
        print self.parent

if __name__ == "__main__":
    print "#"*50
    ffchild = Child()
    ffchild.bar("Chen Beibei")

# the result is almost same as the result without super()
