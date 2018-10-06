from car import Car#导入指定类模块
import car#导入类模块
from electriccar import ElectricCar
my_new_car=Car('audi','a4',2018)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading=23
my_new_car.read_odometer()

my_tesla=ElectricCar('tesla','model s','2018')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
