class NameProperty(object):

    def __init__(self):
        self._name = ''

    def __get__(self, instance, owner):
        print "Getting {}".format(self._name)
        print instance, owner
        return self._name

    def __set__(self, instance, name):
        print "Setting {}".format(name)
        if not isinstance(name, string):
            raise TypeError("name must be a string, but got {}".format(type(name))
        self._name = name.title()

    def __del__(self, instance):
        print "Deleteing {}".format(self._name)
        del self._name


class Person(object):
    name = NameProperty()
    age = 23