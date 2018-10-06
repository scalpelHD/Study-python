class Restaurant():#初次建立和使用类
    """模拟餐馆"""

    def __init__(self,name,cuisine_type):
        """初始化餐馆属性"""
        self.name=name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describle_restaurant(self):
        """打印餐馆信息及有多少人在此就餐"""
        print(self.name.upper()+':')
        print(self.cuisine_type)
        print('There are '+str(self.number_served)+' people being served!')

    def open_restaurant(self):
        """餐馆正在营业"""
        print('The '+self.name.upper()+' is working!')

    def set_number_served(self,num):
        """设置就餐人数"""
        self.number_served=num

    def increment_number_served(self,increase):
        """以递增方式修改就餐人数"""
        self.number_served+=increase

#依据创建的类创建第一个餐馆
restaurant1=Restaurant('Jim\'s restaurant','Sichuan cuisine')
restaurant1.number_served=8
print(restaurant1.name.upper()+':')
print(restaurant1.cuisine_type)
restaurant1.set_number_served(9)
restaurant1.describle_restaurant()
restaurant1.increment_number_served(2)
restaurant1.describle_restaurant()
restaurant1.open_restaurant()

#创建第二个餐馆
restaurant2=Restaurant('Sam\'s restaurant','Guangdong cuisine')
print(restaurant2.name.upper()+':')
print(restaurant2.cuisine_type)
restaurant2.describle_restaurant()
restaurant2.open_restaurant()

#创建第二个类
class User():
    """储存用户的信息"""

    def __init__(self,first,last,location):
        """初始化描述用户信息"""
        self.first=first
        self.last=last
        self.location=location
        self.login_attempts=0

    def describle_user(self,age):
        """描述用户信息"""
        print(str(age)+'-year-old '+self.first.title()+' '+self.last.title()+
              ' is living in '+self.location.title())
        print(str(self.login_attempts)+' users have logged in!')

    def greet_user(self):
        """向用户问好"""
        print('Hi,good morning,'+self.first.title()+' '+self.last.title()+'.')

    def increment_login_attempts(self):
        """将login_attempts加1"""
        self.login_attempts+=1

    def reset_login_attempts(self):
        """将login_attempts重新归零"""
        self.login_attempts=0
        


#依据类创建用户
user0=User('albert','einstein','princeton')
user0.describle_user(23)
user0.increment_login_attempts()
user0.increment_login_attempts()
user0.increment_login_attempts()
user0.describle_user(23)
user0.reset_login_attempts()
user0.describle_user(23)
user0.greet_user()
        
