#coding=gbk

import matplotlib.pyplot as plt
x_values=range(1,1001)
y_values=[value**2 for value in x_values]
plt.scatter(x_values,y_values,s=4,edgecolor='none',c=y_values,cmap=plt.cm.Blues)

#设置图表标题并给坐标轴加上标签
plt.title("Square Number",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize=14)

#设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])

plt.show()
#plt.savefig('squares_plot.png',bbox_inches='tight')
