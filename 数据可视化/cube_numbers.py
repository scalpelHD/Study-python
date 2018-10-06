#coding=gbk

import matplotlib.pyplot as plt

#��������������ֵͼ��
x_values=range(1,5001)
y_values=[x**3 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,edgecolor='none',s=10,cmap=plt.cm.Reds)

#����ͼ������������
plt.title("Cube Numbers",fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Cube of Value',fontsize=14)

#��ǿ̶ȴ�С
plt.tick_params(axis='both',which='major',labelsize=14)

plt.show()
