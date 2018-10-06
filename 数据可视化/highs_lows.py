#coding=gbk
import csv
from matplotlib import pyplot as plt
from datetime import datetime

#从文件中获取最高气温
filename='death_valley_2014.csv'
filename1='sitka_weather_2014.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)

    dates,highs,lows=[],[],[]
    for row in reader:
        try:
            date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low=int(row[3])
        except ValueError:
            print(date,'missing date')
        else:
            lows.append(low)
            highs.append(high)
            dates.append(date)
with open(filename1) as f:
    reader1=csv.reader(f)
    header_row1=next(reader1)

    dates1,highs1,lows1=[],[],[]
    for row in reader1:
        try:
            date1 = datetime.strptime(row[0], '%Y-%m-%d')
            high1 = int(row[1])
            low1=int(row[3])
        except ValueError:
            print(date1,'missing date')
        else:
            lows1.append(low1)
            highs1.append(high1)
            dates1.append(date1)

#根据数据绘制图形
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.plot(dates1,highs1,c='black',alpha=0.5)
plt.plot(dates1,lows1,c='yellow',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
plt.fill_between(dates1,highs1,lows1,facecolor='green',alpha=0.1)

#设置图形格式
plt.title("Daily high and low temperatures-2014",fontsize=24)
plt.xlabel("",fontsize=16)
fig.autofmt_xdate()
plt.ylabel("temperature (F)",fontsize=16)
plt.tick_params(axis="both",which='major',labelsize=16)

plt.show()
