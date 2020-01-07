import  matplotlib.pyplot as plt
'''
input_squares=[1,2,3,4,5]
squares=[1,4,9,16,25]

plt.scatter(input_squares,squares,s=200)#s圆点大小

#设置标签标题
plt.title('Squares Number',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Squares of Value',fontsize=14)

plt.tick_params(axis='both',which='major',labelsize=14)

plt.show()

'''
#scatter分开散开散射  edge color 边缘颜色 cmap 映射 axis轴，轴心 tick_params  标记与——参数
#bbox 盒子 inches英寸 tight密封的
x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]

#plt.scatter(x_values,y_values,s=40,edgecolor='none',c='red')#c可使用RGB
plt.scatter(x_values,y_values,s=40,edgecolor='none',c=y_values, cmap=plt.cm.Reds)#c颜色映射s


#设置标签标题
plt.title('Squares Number',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Squares of Value',fontsize=14)

plt.axis([0,1100,0,1100000])

#plt.show()
plt.savefig('文件名.png',bbox_inches='tight')#bbox_inches是否保留空白区域