class Person(object):

    def __init__(self,first_name,last_name):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        """
        return the full name
        """
        return "{} {}".format(self.first_name,self.last_name)


pp = Person("Mike","Dick")
print pp.full_name


pp.full_name = 'zzz zzz'
