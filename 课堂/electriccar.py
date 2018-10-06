from car import Car
class Battery():
    """模拟电动车汽电瓶"""
    def __init__(self,battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size=battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print('This car has a '+str(self.battery_size)+'-kwh battery.')

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=270

        message='This car can go approximately '+str(range)
        message+=' miles on a full charge.'
        print(message)

class ElectricCar(Car):
    """一方面是汽车，一方面又是特殊的电动交通工具"""

    def __init__(self,make,model,year):
        """
        电动汽车的独特之处
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make,model,year)
        self.battery=Battery()

    def fill_gas_tank(self):#子类重写从父类继承的方法
        """电动汽车没有油箱"""
        print('This car does\'t need a gas tank!')
