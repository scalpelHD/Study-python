class Car():
    """一次模拟汽车的尝试"""

    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print('This car has '+str(self.odometer_reading)+' miles on it.')

    def update_odometer(self,mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage>+self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print('You can\'t roll back an odometer!')

    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        if miles>=0:
            self.odometer_reading+=miles
        else:
            print('The incresement can\'t smaller than zero!')

    def fill_gas_tank(self,scale):
        """描述油箱大小"""
        print('The car has a '+str(scale)+' L tank.')

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

    def upgrade_battery(self):
        """给电瓶升级"""
        if self.battery_size!=85:
            self.battery_size=85

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

electriccar=ElectricCar('tesla','A4',2018)
electriccar.battery.get_range()
electriccar.battery.upgrade_battery()
electriccar.battery.get_range()
