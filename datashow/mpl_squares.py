import  matplotlib.pyplot as plt

input_squares=[1,2,3,4,5]
squares=[1,4,9,16,25]

plt.plot(input_squares,squares,linewidth=5)#linewidth 线条粗细 x,y
#设置标签标题
plt.title('Squares Number',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Squares of Value',fontsize=14)
#刻度样式以及字体大小
plt.tick_params(axis='both',labelsize=14)
plt.show()