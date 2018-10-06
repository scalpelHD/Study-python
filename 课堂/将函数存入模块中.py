from 传递任意数量的实参 import build_profile#导入特定函数
import pizza#导入不特定函数

user_profile=build_profile('albert','einstein',
                           location='princeton',
                           filed='physics')
print(user_profile)
pizza.make_pizza(16,'mushroom','extra cheese')#导入不特定函数时引用函数
                                              #要使用句点

from pizza import make_pizza as mp#导入函数时给函数指定别名
mp(12,'green pepper','mushroom')

import pizza as p#导入模块时给模块指定别名（重复导入会覆盖原有导入）
#错误重复导入：from p import make_pizza as mp
p.make_pizza(12,'green pepper','extra cheese')

from 传递任意数量的实参 import *#使用*导入模块中所有的函数调用时无需使用句点
make_new_pizza(12,'mushroom','grren pepper')



