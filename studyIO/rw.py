#coding=utf-8


try:
    f = open('/Users/yy/pythonS/python_study/txtIo.txt', 'r')
    print '文件内容：', f.read()
    print '文件名：', f.name
    print '是否已关闭：', f.closed
    print '访问模式：', f.mode
finally:
    if f:
        f.close()


with open('/Users/yy/pythonS/python_study/txtIo.txt', 'rb') as f:
    print 'rb:', f.read()

# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复
# 调用read(size)方法，每次最多读取size个字节的内容。另外，
# 调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。

with open('/Users/yy/pythonS/python_study/txtIo.txt', 'r') as f:
    for line in f.readlines():
        print 'r:', (line.strip())





# file-like Object

# 像open()函数返回的这种有个read()方法的对象，
# 在Python中统称为file-like Object。
# 除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。
# StringIO就是在内存中创建的file-like Object，常用作临时缓冲。
with open('/Users/yy/pythonS/python_study/txtIo.txt', 'w') as fw:
    fw.write('Hello,world!')

with open('/Users/yy/pythonS/python_study/txtIo.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())
