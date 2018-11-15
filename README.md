# notifyr - *Create observers in runtime*
PyPi: https://pypi.org/project/notifyr/

## Description
  Notifyr is a package that enables simple class observed-observer schema at runtime. Instead of building the whole observation and notification toolchain, just use python decorators and notifyr will take care of the rest.

  Inspired by the Observer Design Pattern, notifyr adds the necessary methods to your classes without inheritance.

## Decorators
Function decorators:
- `@target`
    - Indicates that the decorated function is targeted and will trigger the observers `update()` everytime it runs.

Class decorators:
- `@observed`
    - Adds `.observers` list attribute.
    - Adds `.attach(obj)` method that appends `obj` to the observers list.
    - Adds `.notify()` method that notifies the observers everytime the targeted functions are called
- `@observer('function_name')`
    - Adds `update()` method that executes class's `function_name()` passing, as arguments, `self` and everything that the targeted function received (including the `self` argument).  

## Usage
Original Code:


``` python
class Dog(object):
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print('Woof')
    
    def sleep(self):
        print(self.name, 'is now asleep: ZZzzzzZzzZ...')

class Person(object):
    def __init__(self, name):
        self.name = name
    
    def educate_dog(self, dog):
        print(self.name + ':','Sleep,', dog.name)
        dog.sleep()
```

Suppose we want a person to educate a dog every time the animal barks:

``` python
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
```

And now, it is possible to archieve this by magically calling `bark()` after attaching a person to a dog:

```python
d = Dog('Tobby')
p = Person('Victor')

d.attach(p) # Victor is now observing Tobby

d.bark()
# Woof
# Victor: Sleep, Tobby
# Tobby is now asleep: ZZzzzzZzzZ...
```
