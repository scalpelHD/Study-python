import unittest
from city_function import city_country

class Testcitycountry(unittest.TestCase):
    """测试ciy_country"""

    def testcitycountry(self):
        temp=city_country('Chengdu','China',population=5000000)
        self.assertEqual(temp,'Chengdu,China-population:5000000')

unittest.main()
