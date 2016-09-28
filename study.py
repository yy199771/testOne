#coding=utf-8
import linecache
import time

now = time.time() #代码开始时间

# 前期准备，整理数据
data_keys = ('bid', 'uid', 'username', 'v_class', 'content', 'img', 'created_at', 'source', 'rt_num', 'cm_num', 'rt_uid', 'rt_username', 'rt_v_class', 'rt_content', 'rt_img', 'src_rt_num', 'src_cm_num', 'gender', 'rt_bid', 'location', 'rt_mid', 'mid', 'lat', 'lon', 'lbs_type', 'lbs_title', 'poiid', 'links', 'hashtags', 'ats', 'rt_links', 'rt_hashtags', 'rt_ats', 'v_url', 'rt_v_url')

print "data_keys:%d" %len(data_keys)

keys = {data_keys[k]:k for k in xrange(0,len(data_keys))}

f = linecache.getlines('tt.txt')

lines = [x[1:-1].split('","') for x in f] #拆分

#1 输出用户总数

users = set([line[keys['username']] for line in lines])

print "users: %s" %users

user_total = len(set(users))

print user_total

assert type(user_total) == int