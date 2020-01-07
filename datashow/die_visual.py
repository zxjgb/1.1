#-*- coding=utf-8 -*-
from die import Die
from  random import randint
import pygal

die1=Die()
results=[]
for roll_num in  range(10000):
	result=die1.roll()
	results.append(result)
print (results)

frequencies=[] #频率，频次分析

for value in range(1,die1.num_sides+1):
	frequency=results.count(value)
	frequencies.append(frequency)
print (frequencies)

hist=pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result" 
hist.y_title = "Frequency of Result"
hist.add('D6', frequencies) 
hist.render_to_file(r"C:\Users\ZXJ\Desktop\die_visual.svg")