from matplotlib import pyplot as plt
from datetime import datetime
import csv

class Figure():
    """绘制天气图表的类"""

    def __init__(self,filename):
        """初始化属性"""
        self.filename=filename
        self.reader=0
        self.dates,self.highs,self.lows = [], [], []

    def read_data(self):
        """读取数据"""
        with open(self.filename ) as f:
            self.reader=csv.reader(f)
            header_row=next(self.reader)

            for row in self.reader:
                try:
                    date=datetime.strptime(row[0],"%Y-%m-%d")
                    high=int(row[1])
                    low=int(row[3])
                except ValueError:
                    print(date,"missing data")
                else:
                    self.dates.append(date)
                    self.highs.append(high)
                    self.lows.append(low)


    def draw_figure(self):
        """绘制图表"""
        fig=plt.figure(dpi=128,figsize=(10,6))
        plt.plot(self.dates,self.highs,c='red',alpha=0.5)
        plt.plot(self.dates,self.lows,c='blue',alpha=0.5)
        plt.fill_between(self.dates,self.highs,self.lows,facecolor='blue',alpha=0.1)

        """设置图表格式"""
        plt.title('Daily high and low temperatures-2014',fontsize=24)
        plt.xlabel('',fontsize=16)
        plt.ylabel('Temperature (F)',fontsize=16)
        plt.tick_params(axis='both',which='major',labelsize=16)


    def show_figure(self):
        plt.show()


filename='death_valley_2014.csv'
death_valley=Figure(filename)
death_valley.read_data()
death_valley.draw_figure()
death_valley.show_figure()

filename1='sitka_weather_2014.csv'
sitka=Figure(filename1)
sitka.read_data()
sitka.draw_figure()
sitka.show_figure()

