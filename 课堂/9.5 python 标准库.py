from random import randint
from collections import OrderedDict

class Die():
    """模拟骰子"""
    def __init__(self,side=6):
        """骰子有六个面"""
        self.side=side

    def roll_die(self):
        """模拟掷骰子"""
        return randint(1,6)


favorite_language=OrderedDict()
favorite_language={'jen':'python','sarah':'c','edward':'ruby','phil':'python'}

for name,language in favorite_language.items():
    print(name.title()+'\'s favorite language is '+
          language.title()+'.')

diew=Die()
i=0
while i<10:
              print(diew.roll_die())
              i+=1
              
              
