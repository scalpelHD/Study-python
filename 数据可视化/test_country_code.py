import unittest
from country_code import get_country_code as gcc

class Testgcc(unittest.TestCase):
    """测试gcc函数"""

    def test_gcc(self):
        reply=gcc('Mexico')
        self.assertEqual(reply,'mx')

unittest.main()