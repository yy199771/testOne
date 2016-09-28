#coding=utf-8
import glob
'''
1. 可选参数，是有默认值的；
2。必须参数，是没有默认值的。
默认值与没有默认值的区别在于 “=”

函数的健壮性
1.你永远知道你的方法会返回什么（异常处理，条件判断）
2.返回你想要的结果

断言：
assert 常用的测试方法


def add(num1,num2):
    if isinstance(num1,int) and isinstance(num2, int):
        return num1 + num2
    else:
        return '参数里面有不是数字的类型.'
print add('adfa',19)

assert add(1,2)==3
assert add(1,4)==3
'''

'''
习题：
1.定义一个方法 func，该func可以引入任意多的整型参数，结果返回其中最大与最小的值。
2.定义一个方法func，该func可以引入任意多的字符串参数，结果返回（长度）最长的字符串。
3.定义一个方法get_doc(module)，module参数为该脚本中导入或定义的模块对象，该函数返回module的帮助文档。
例 print get_doc(urllib),则会输出urllib这个模块的帮助文档。
4.定义一个方法get_text(f),f参数为任意一个文件的磁盘路径，该函数返回f文件的内容。
5.定义一个方法get_dir(folder),folder参数为任意一个文件夹，该函数返回folder文件夹的文件列表。提示（可以了解python的glob模块）
'''

# 定义可变参数喝定义list或tuple参数相比,仅仅在参数前面加了一个"*"号.
# 关键字参数:可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。

def func11(*num):
    for i in num:
        if not isinstance(i,int):
            return "输入的参数必须为整形。"
    a = sorted(num)
    return 'Min:%s'%a[0],'Max:%s'%a[-1]
print func11(1,23,32,42,533,2,123,22,12)

def func2(*str):
    if isinstance(str,tuple):
        length = 0
        for i in range(0,len(str)):
            if length < len(str[i]):
                length = len(str[i])
                max =str[i]
        return max,len(max)
    else:
        return 'error'
print func2('abc','ererera','aa','fdafdasfdsafdsfsdafsdfdsaf','a')
#获取module的帮助
def get_doc(module):
    return help(module)
#print get_doc('os')

#get_dir(folder)
def get_dir(folder):
    return glob.glob(folder)
print get_dir(r"D:/python_finance/*/*.py")




