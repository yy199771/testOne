# coding=utf-8

import time
import calendar

localtime = time.asctime(time.localtime(time.time()))
print '本地时间：', localtime

#print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print time.ctime()


cal = calendar.month(2016,1)
#print '以下输入2016年1月份的日历：'
#print cal