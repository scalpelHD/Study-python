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

class IceCreamStand(Restaurant):
    """描述冰淇淋小店，一种特殊的餐馆"""

    def __init__(self,name,cuisine_type):
        """继承餐馆的类"""
        super().__init__(name,cuisine_type)
        self.flavors=['strawberry ice cream','apple ice cream',
                      'vanilla ice cream']

    def describe_icecream_type(self):
        """显示冰淇淋的种类"""
        print('Sam\'s ice wood serve following flavors:')
        for type in self.flavors:
            print('--'+type)
        

sam_ice_wood=IceCreamStand('sam\'s ice cream','sweet dessert')
sam_ice_wood.describle_restaurant()
sam_ice_wood.describe_icecream_type()

