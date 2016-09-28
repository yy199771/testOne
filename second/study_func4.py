#coding=utf-8
"""
进阶 函数 第四节

step1:童鞋们的习题反馈

step2:lambda之再议

	1.lambda是一个表达式。
	2.它没有名称，存储的也不是代码块，而是表达式。
	3.它被用作执行很小的功能，不能在里面使用条件语句。

step3:函数参数总结

	1.位置匹配 func(name)
	2.关键字匹配 func(key=value)
	3.收集匹配
			1.元组收集 func(name,arg1,arg2)
			2.字典收集 func(name,key1=value1,key1=value2)
	4.参数顺序

step4:接触递归

	1.递归是调用自身
	2.理解下面的函数




def func(arg1,arg2,arg3):
	return arg1,arg2,arg3

print func(1,2,3)

def func1(k1='',k2=None,k3=''):
	return k1,k2,k3

print func1(k3=5,k1=4,k2=3)




* kargs 元组

** kwargs 字典


参数位置：

1.先是位置匹配的参数
2.再是关键字匹配的参数
3.收集匹配的元组参数
4.收集匹配的关键字参数





def func2(a,d,b=4,*kargs,**kwargs):
	return kargs


print func2(2,3,4,5,6,7,9,[1,2,3,4],{1:2,3:4})




# d = lambda x:x+1 if x > 0 else "error"

# g = lambda x:[(x,i) for i in xrange(0,10)]


# def e(x):
# 	return x+1


# t = [1,2,3,4,5]

# g = filter(lambda x:x > 3,t)


# print d(2)
# print d(4)
# print d(5)
# print d(-1)
# print d(-2)

# #print g(10)

# print g



def func1(i):
	if i<100:
		return i + func1(i+1)
	return i
print func1(0)
"""