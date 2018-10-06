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
        self.login_attempts+=1
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

class Privileges():
    """编写大类中的小类"""
    def __init__(self):
        self.privileges=['can add post','can delete post','can ban user']

    def show_privileges(self):
        """显示管理员的权限"""
        print('Dear ADMINISTOR,you have some privileges as following:')
        for privilege in self.privileges:
            print('-'+privilege)    

class Admin(User):
    """建立管理员的类，并继承用户的类"""

    def __init__(self,first,last,location):
        """继承用户类"""
        super().__init__(first,last,location)
        self.privileges=Privileges()


admin=Admin('hoow','tongue','Sichuan')
admin.describle_user(20)
admin.privileges.show_privileges()
