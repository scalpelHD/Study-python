#coding=gbk

from random import choice
import matplotlib.pyplot as plt

class RandWalk():
	"""一个生成随机漫步数据的类"""
	
	def __init__(self,num_points=5000):
		"""初始化随机漫步的属性"""
		self.num_points=num_points
		
		#所有随机漫步都始于（0，0）
		self.x_values=[0]
		self.y_values=[0]
		
		
	def get_step(self):
		"""确定漫步方向和距离"""
		#决定前进方向以及沿这个方向前进的距离
		direction=choice([1,-1])
		distance=choice([0,1,2,3,4])
		return direction*distance
		
		
	def fill_walk(self):
		"""计算随机漫步包含的所有点"""
		
		#不断漫步，直到列表达到指定的长度
		while len(self.x_values) < self.num_points:
			x_step=self.get_step()
			y_step=self.get_step()
			
			#拒绝原地踏步
			if x_step == 0 and y_step == 0:
				continue
				
			#计算下一个点的x值和y值
			next_x=self.x_values[-1]+x_step
			next_y=self.y_values[-1]+y_step
			
			self.x_values.append(next_x)
			self.y_values.append(next_y) 
while True:
	#创建RandWalk实例，并绘图
	rw=RandWalk(50000)
	rw.fill_walk()
	
	point_numbers=list(range(rw.num_points))
	#设置绘图窗口的尺寸
	plt.figure(figsize=(10,6))
	plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,
	edgecolor='none',s=1)
	
	#突出起点和终点
	plt.scatter(0,0,c='green',edgecolor='none',s=100)
	plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none',
	s=100)
	
	#隐藏坐标轴
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	
	#绘图
	plt.show()

	keep_running=input('Make another walk?')
	if keep_running == 'n':
		break
			
