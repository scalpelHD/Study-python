import matplotlib.pyplot as plt
from die import Die

die0=Die()
die1=Die()
x_values=range(1,1001)
y_values=[]
for value in range(1000):
    result=die0.roll()+die1.roll()
    y_values.append(result)
plt.plot(x_values,y_values,linewidth=4)

#设置图表标题并给坐标轴加上标签
plt.title("The result of 2 D6 1000 times in matplotlib",fontsize=24)
plt.xlabel("The time",fontsize=14)
plt.ylabel("The number",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both',labelsize=14)

#设置每个坐标轴的取值范围
plt.axis([1,1001,2,12])

plt.show()
