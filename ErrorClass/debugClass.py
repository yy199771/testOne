#coding=utf-8

# 调试-------------------
import logging
logging.basicConfig(level=logging.INFO)
import unittest
from myDict import Dict


# 断言 assert

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / 0

def main():
    foo('1')

# main()

# logging
# pdb
'''
s = '0'
n = int(s)
logging.info('n = %d' %n)
print 10 / n
# pdb

ss = 'n'
nn = int(ss)
print 10 / n
'''

class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEquals(d.a,1)
        self.assertEquals(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEquals(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ =='__main__':
    unittest.main()


