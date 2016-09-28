#coding=utf-8

#多重继承
'''
在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。
但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。
这种设计通常称之为Mixin。

为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixin和FlyableMixin。
类似的，你还可以定义出肉食动物CarnivorousMixin和植食动物HerbivoresMixin，让某个动物同时拥有好几个Mixin：
'''
#动物
class Animal(object):
    pass

#动作行为
class RunnableMixin(object):
    def run(self):
        print 'Running...'

class FlyableMixin(object):
    def fly(self):
        print 'Flying...'

#大类
class Manmal(Animal):
    pass

class Bird(Animal):
    pass

#各种动物
class Dog(Manmal, RunnableMixin):  #多重继承
    pass

class Bat(Animal, FlyableMixin):
    pass

class Parrot(Animal):
    pass


