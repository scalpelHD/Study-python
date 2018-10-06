def greet_user(username):
    """显示简单的问候语"""
    print("Hello,"+username.title()+'!')
greet_user('Anna')
def describle_pet(pet_name,animal_type='dog'):#当设定默认值时需要注意位置关系
    """显示宠物的信息"""
    print('\nI have a '+animal_type+'.')
    print('My '+animal_type+"'s name is "+pet_name.title()+'.')
#多种传递实参的调用函数的方法
describle_pet('harry','hamster')
describle_pet(pet_name='tom',animal_type='cat')
describle_pet(pet_name='tony')
describle_pet('sam','goldfish')
describle_pet(animal_type='snake',pet_name='rainbow')
