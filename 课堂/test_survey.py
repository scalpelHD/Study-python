import unittest
from survey import Survey

class TestSurvey(unittest.TestCase):
    """针对Survey类的测试"""

    def setUp(self):
        """
        创建一个对象和一组答案，供使用的测试方法使用
        """
        question='What language did you first learn to speak?'
        self.my_survey=Survey(question)
        self.responses=['English','Chinese','Spanish','Korea']

    def test_store_single_response(self):
        """测试单个答案会被妥善的储存"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善的储存"""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)
            

unittest.main()
