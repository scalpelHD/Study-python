class Employee():
    """模拟雇员"""

    def __init__(self,first,last,salary):
        """初始化雇员属性"""
        self.name=first.title()+' '+last.title()
        self.salary=salary

    def give_raise(self,add=''):
        """涨工资"""
        if add:
            self.salary+=add
        else:
            self.salary+=5000
