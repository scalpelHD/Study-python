#coding=gbk

from random import choice
import matplotlib.pyplot as plt

class RandWalk():
	"""һ����������������ݵ���"""
	
	def __init__(self,num_points=5000):
		"""��ʼ���������������"""
		self.num_points=num_points
		
		#�������������ʼ�ڣ�0��0��
		self.x_values=[0]
		self.y_values=[0]
		
		
	def get_step(self):
		"""ȷ����������;���"""
		#����ǰ�������Լ����������ǰ���ľ���
		direction=choice([1,-1])
		distance=choice([0,1,2,3,4])
		return direction*distance
		
		
	def fill_walk(self):
		"""��������������������е�"""
		
		#����������ֱ���б�ﵽָ���ĳ���
		while len(self.x_values) < self.num_points:
			x_step=self.get_step()
			y_step=self.get_step()
			
			#�ܾ�ԭ��̤��
			if x_step == 0 and y_step == 0:
				continue
				
			#������һ�����xֵ��yֵ
			next_x=self.x_values[-1]+x_step
			next_y=self.y_values[-1]+y_step
			
			self.x_values.append(next_x)
			self.y_values.append(next_y) 
while True:
	#����RandWalkʵ��������ͼ
	rw=RandWalk(50000)
	rw.fill_walk()
	
	point_numbers=list(range(rw.num_points))
	#���û�ͼ���ڵĳߴ�
	plt.figure(figsize=(10,6))
	plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,
	edgecolor='none',s=1)
	
	#ͻ�������յ�
	plt.scatter(0,0,c='green',edgecolor='none',s=100)
	plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none',
	s=100)
	
	#����������
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	
	#��ͼ
	plt.show()

	keep_running=input('Make another walk?')
	if keep_running == 'n':
		break
			
