#coding=utf-8
'''
进阶 函数 第三节
1.习题反馈
2.自省与函数
 func.__code__
3.作用域问题再议
    global：全局变量关键字
4.可变参数的魔法与禁忌
    为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。
    此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。

Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，运行会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
'''
def func1(arg1,arg2):
    return arg1 * arg2

#print dir(func1.__code__)

#print dir(func1.__code__.co_varnames)
#print dir(func1.__code__.co_filename)

"""
今天习题：
1 定义一个方法get_fundoc(func),func参数为任意一个函数对象，返回该函数对象的描述文档，如果该函数没有描述文档，则返回"not found"
2 定义一个方法get_cjsum(),求1-100范围内的所有整数的平方和。返回结果为整数类型。
3 定义一个方法list_info(list), 参数list为列表对象，怎么保证在函数里对列表list进行一些相关的操作，不会影响到原来列表的元素值，比如：

a = [1,2,3]

def list_info(list):
   '''要对list进行相关操作，不能直接只写一句return[1,2,5]，这样就没意义了'''

print list_info(a):返回结果：[1,2,5]

print a 输出结果：[1,2,3]

写出函数体内的操作代码。

4 定义一个方法get_funcname(func),func参数为任意一个函数对象，需要判断函数是否可以调用，如果可以调用则返回该函数名(
类型为str)，否则返回 “fun is not function"。
"""
#1 定义一个方法get_fundoc(func),func参数为任意一个函数对象，返回该函数对象的描述文档，如果该函数没有描述文档，则返回"not found"
def get_fundoc(func):
    if not isinstance(func,object):
        return "参数不是一个对象。"
    if func.__doc__ is None:
        return 'not found'
    else:
        return func.__doc__

#print get_fundoc(func1(1,2))
print get_fundoc([1,2,3])