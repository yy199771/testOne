#coding=utf-8

# 定制类 形如:__slots__,这些在Python中是有特殊用途的.

#__str__
class Student():
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name

print Student('Jack')

s = Student('Jack')
print s.name

# __iter__

# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1    # 初始化两个计数器a, b

    def __iter__(self):
        return self    # 实例本身就是迭代对象,故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b    #计算下一个值
        if self.a > 100:    # 退出循环的条件
            raise StopIteration();
        return self.a   # 返回下一个值

for n in Fib():
   print n

# __getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
# 但是list有个神奇的切片方法：
# 对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断

class Fib1(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
f = Fib1()
print f[40]
print f[0:8]
