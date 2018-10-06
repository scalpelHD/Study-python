#coding=gbk

import matplotlib.pyplot as plt

#绘制整数的立方值图表
x_values=range(1,5001)
y_values=[x**3 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,edgecolor='none',s=10,cmap=plt.cm.Reds)

#设置图表标题和坐标轴
plt.title("Cube Numbers",fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Cube of Value',fontsize=14)

#标记刻度大小
plt.tick_params(axis='both',which='major',labelsize=14)

plt.show()
