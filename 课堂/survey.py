class Survey():
    """收集匿名调查问卷的答案"""

    def __init__(self,question):
        """储存一个问题，并为储存答案做准备"""
        self.question=question
        self.responses=[]

    def show(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self,new_response):
        """储存调查问卷的答案"""
        self.responses.append(new_response)

    def show_result(self):
        """显示收集到的所有答卷"""
        print('Survey result:')
        for response in self.responses:
            print('-'+response)
