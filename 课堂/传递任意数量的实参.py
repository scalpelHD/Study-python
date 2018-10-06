def make_pizza(*toppings):#传递任意数量的实参
    """概述要制作的披萨"""
    print('\nMaking a pizza witn the following toppings:')
    for topping in toppings:
        print('-'+topping)
        
#make_pizza('pepperoni')
#make_pizza('mushroom','green peppers','extra cheese')

def make_new_pizza(size,*toppings):#结合位置实参时，任意数量的实参要放最后
    """概述要制作的披萨"""
    print('\ndMake a '+str(size)+
          '-inch pizza with the following toppings:')
    for topping in toppings:
        print('-'+topping)

#make_new_pizza(16,'peppperoni')
#make_new_pizza(12,'mushroom','green pepper','extra cheese')

def build_profile(first,last,**user_info):#使用任意数量的关键字实参
    """创建一个字典，其中包含我们知道的关于用户的一切"""
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile

#user_profile=build_profile('albert','einstein',
                          # location='princeton',
                          # filed='physics')
#print(user_profile)
