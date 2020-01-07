
from die import Die
import pygal

die1=Die()
die2=Die(10)
results=[]
for roll_num in range(1000):
    result=die1.roll()+die2.roll()
    results.append(result)

frequencies=[]
for value in range(2,die1.num_sides+die2.num_sides+1):
    frequency=results.count(value)
    frequencies.append(frequency)

import pygal
hist=pygal.Bar()  
hist._title="Result of rolling one D6 1000 times."
hist.x_labels=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
hist._x_title="Result"
hist._y_title="Frequency of Result"
hist.add('D6,D10',frequencies)  
hist.render_to_file(r"C:\Users\ZXJ\Desktop\die_visual.svg")
