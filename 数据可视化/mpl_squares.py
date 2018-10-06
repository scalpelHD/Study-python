import matplotlib.pyplot as plt

input_values=range(1,11)
squares=[value**2 for value in range(1,11)]
plt.plot(input_values,squares,linewidth=5)

#设置图表标题，并给坐标轴加上标签
plt.title('Square Numbers',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Square of Value',fontsize=14)
#设置刻度大小
plt.tick_params(axis='both',labelsize=14)
plt.show()
