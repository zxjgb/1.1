from randomwalk import Random_walk
import  matplotlib.pyplot as plt


while True:
	rw=Random_walk(50000)
	rw.fill_walk()
	plt.figure(dpi=1280,figsize=(10,100))#函数figure()用于指定图表的宽度、高度、分辨率和背景色。
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values,rw.y_values,s=1,edgecolor='none',c=point_numbers,cmap=plt.cm.Blues)
	plt.scatter(0,0,s=100,c='green',edgecolor='none')
	plt.scatter(rw.x_values[-1],rw.y_values[-1],s=100,c='red',edgecolor='none')
	plt.axes().get_xaxis().set_visible(False)#隐藏任务
	plt.axes().get_yaxis().set_visible(False)
	plt.show()
	keeping=input('Make another walk?y/n')
	if keeping=='n':
	
		break