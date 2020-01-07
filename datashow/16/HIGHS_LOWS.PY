# -*- coding:utf-8 -*-
import  matplotlib.pyplot as plt
import csv
from datetime import datetime

filename=r'C:\Users\ZXJ\Desktop\datashow\16\data\sitka_weather_2018_full.csv'

with open(filename) as f:
	reader=csv.reader(f)
	header_row=next(reader)
	print(header_row)
    
	datas,highs,lows=[],[],[]
	for row  in  reader:
		highs.append(row[8])
		lows.append(row[9])
		current_date = datetime.strptime(row[2], "%Y-%m-%d")
		datas.append(current_date)
	print (highs)
	
	fig=plt.figure(dpi=128,figsize=(12,10))
	plt.plot(datas,highs, c='red',alpha=0.5)
	plt.plot(datas,lows, c='blue',alpha=0.5)
	plt.fill_between(datas, highs, lows, facecolor='blue', alpha=0.1)
	#设置标签标题
	plt.title('Daily high temperatures, July 2014',fontsize=24)
	plt.xlabel('',fontsize=14)
	fig.autofmt_xdate()
	plt.ylabel('Temperature (F)',fontsize=14)
	#刻度样式以及字体大小
	plt.tick_params(axis='both',which='major',labelsize=16)
	
	plt.show()