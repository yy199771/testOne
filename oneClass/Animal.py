#coding='UTF-8'

import types

class Animal(object):
    def run(self):
        print 'Animal is running.'

class Dog(Animal):
    def run(self):
        print 'Dog is running.'

class Cat(Animal):
    def run(self):
        print 'Cat is running.'

def run_twice(animal):
    animal.run()
    animal.run()

dog = Dog()
dog.run()
cat = Cat()
cat.run()
run_twice(Animal())
run_twice(Dog())

print type(Animal())

print type('abc') == types.StringType

print isinstance(Animal(),int)
