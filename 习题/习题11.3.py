import unittest
from 习题113配套 import Employee

class TestEmployee(unittest.TestCase):
    """测试Employee类"""

    def setUp(self):
        """创建实例"""
        self.worker=Employee('peter','smith',5000)

    def test_give_default_raise(self):
        """测试未指定增量"""
        self.worker.give_raise()
        self.assertEqual(10000,self.worker.salary)

    def test_give_custom_raise(self):
        """测试指定增量"""
        self.worker.give_raise(1000)
        self.assertEqual(6000,self.worker.salary)

unittest.main()
