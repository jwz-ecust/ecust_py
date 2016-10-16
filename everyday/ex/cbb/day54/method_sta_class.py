class Helloworld(object):
    def __init__(self):
        print 'Init Hello World'

    @staticmethod
    def hello_static(name):
        print "hello_static(): Hello %s" %name
        print

    @classmethod
    def hello_class(cls,name):
        print "hello_class():hello %s" %name
        print "Now call hello_static():"
        cls.hello_static(name)
        print

    def hello_world(self,name):
        print "hello world: Hello %s" %name

Helloworld.hello_static("static")

Helloworld.hello_class('class')

haha = Helloworld()

haha.hello_world('hw.static')
haha.hello_world("hw.class")