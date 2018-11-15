from notifyr.agents import observed, observer
from notifyr.functions import target

@observed
class Dog(object):
    def __init__(self, name):
        self.name = name
    
    @target
    def bark(self):
        print('Woof')
    
    def sleep(self):
        print(self.name, 'is now asleep: ZZzzzzZzzZ...')
    
@observer('educate_dog')
class Person(object):
    def __init__(self, name):
        self.name = name
    
    def educate_dog(self, dog):
        print(self.name + ':','Sleep,', dog.name)
        dog.sleep()

if __name__ == "__main__":
    d = Dog('Tobby')
    p = Person('Victor')

    d.attach(p) # Victor is now observing Tobby

    d.bark()
    # Woof
    # Victor: Sleep, Tobby
    # Tobby is now asleep: ZZzzzzZzzZ...