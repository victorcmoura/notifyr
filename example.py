from notifyr.agents import observer, observed
from notifyr.functions import target

@observed('get_owners')
class Dog(object):
    def __init__(self, name):
        self.name = name
        self.owners = []

    @target
    def bark(self):
        print('Woof')

    def sleep(self):
        print('ZZzzZZZzZzZ')

    def get_owners(self):
        return self.owners

    def add_owner(self, owner):
        self.owners.append(owner)

@observer('educate_dog')
class Owner(object):
    def __init__(self, name):
        self.dogs = []
        self.name = name

    def educate_dog(self, dog):
        dog.sleep()


d = Dog('Tobby')
d.bark()

o = Owner('Victor')
d.add_owner(o)

d.bark()
