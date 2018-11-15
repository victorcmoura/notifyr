from notifyr.agents import observer, observed
from notifyr.functions import target

@observed
class Dog(object):
    def __init__(self, name):
        self.name = name

    @target
    def bark(self):
        print('Woof')

    def sleep(self):
        print('ZZzzZZZzZzZ')

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
d.attach(o)

d.bark()
