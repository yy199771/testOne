#coding=utf-8
import urllib


'''
1.怎么去学习使用函数

	（1）别管那么多复杂的，先直接把功能实现了。
	（2）抽象成函数：命名规范，伪代码,参数默认值。
	（3）将函数变得更健壮，让它可以跑很多地方
					1.假设你写的函数是要交给你的基友用 -》 功能完整
					2.假设你写的函数是要交给你的学弟用 -》 异常处理完善
	(4) 测试
					1.assert
					2.对函数的返回进行一个值和类型的测试。
					3.单元测试

def func1(a,b,c,d,e):
	“”“
	@a:

	”“”
	pass

下划线命名线  get_doc
驼峰命名法 getDocFromUrl

为什么要用默认值：
1.更省事
2.更可配置
'''

"""
习题：
1 定义一个方法get_num(num),num参数是列表类型，判断列表里面的元素为数字类型。其他类型则报错，并且返回一个偶数列表：（注：列表里面的元素为偶数）。
2 定义一个方法get_page(url),url参数是需要获取网页内容的网址，返回网页的内容。提示（可以了解python的urllib模块）。
3 定义一个方法 func，该func引入任意多的列表参数，返回所有列表中最大的那个元素。
4 定义一个方法get_dir(f),f参数为任意一个磁盘路径，该函数返回路径下的所有文件夹组成的列表，如果没有文件夹则返回"Not dir"。
"""
def get_num(num):
    a = []
    if not isinstance(num,list):
        return "输入参数不是list。"
    for x in num:
        if not isinstance(x,int):
            return "列表中参数类型不是数字。"
        else:
            if x % 2 != 0:
                pass
            else:
                a.append(x)
    return a

assert get_num([1,2,3,4,5,6,7,8,9,10]) == [2,4,6,8,10]
assert get_num(123) == "输入参数不是list。"
assert get_num('123') == "输入参数不是list。"
assert get_num(['123','abc','eere']) == "列表中参数类型不是数字。"
#print get_num([1,2,3,4,5,6,7,8,9,10])

def get_page(url):
    f = urllib.urlopen(url)
    if f.getcode() != 200:
        return "此URL返回不正常。"
    firstLine =f.read()
    head = f.info()
    print head
    return firstLine

#assert get_page('aaaaaaa') == "无法正确的返回url。"
#print get_page('http://www.baidu.com')

#3 定义一个方法 func，该func引入任意多的列表参数，返回所有列表中最大的那个元素。
def func(*nList):
    max = 0
    for n in nList:
        if not isinstance(n,list):
            return "不是一个列表。"
    for x in nList:
        if len(x) > max:
            max = len(x)
            print max
            print x
    return x
print func([1],[2,7],[3,4,5,6,7,8,9,0],[2,3],[4,5,6],[3,67])