#coding=utf-8

class Student():
    pass

#定义一个函数作为实例方法
def set_age(self, age):

    self.age = age

def set_score(self, score):
    self.score = score

from types import MethodType

s = Student()
s.name = 'Michael'
print s.name

#给一个实例绑定的方法,对另一个实例是不起作用的.
s.set_age = MethodType(set_age, s, Student) #给实例绑定一个方法
s.set_age(25)
print s.age

#给calss绑定方法,这样讲对所有的实例有效
Student.set_score = MethodType(set_score, None, Student)
s2 = Student()
s2.set_score(100)
print s2.score

s3 = Student()
s3.set_score(88)
print s3.score

#使用__slots__ 限制class属性:__slots__仅对当前类有效,继承类无效
class Student2():
    __slots__ = ('name', 'age') #用tuple定义允许绑定的属性名称

Student2.set_score = MethodType(set_score, None, Student2)
Student2.set_age = MethodType(set_age, None, Student2)


ss = Student2()
ss.name = 'Jack'
print ss.name

ss.age = 25
print ss.age

ss.set_score = 101
print ss.score